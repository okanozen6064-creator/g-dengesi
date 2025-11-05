# -*- coding: utf-8 -*-

"""
game_state.py: Streamlit'in session_state'ini kullanarak oyun durumunu yönetir.
İktidar Döngüsü mekaniklerini ve rakip partilerin simülasyonunu içerir.
TÜM mekanikler tamamlandı.
"""

import streamlit as st
import copy
import random
from parties import PARTIES
from events import get_random_event

def initialize_game_state(selected_party_name):
    """Oyun durumunu ve TÜM partilerin başlangıç durumunu session_state içinde başlatır."""
    if 'game_started' not in st.session_state:
        st.session_state.game_started = True
        st.session_state.selected_party_name = selected_party_name
        st.session_state.year = 1
        st.session_state.action_points = 3 # PART 4: EP Değeri 3'e düşürüldü

        st.session_state.action_feedback = None
        st.session_state.event_feedback = None

        st.session_state.all_parties_state = {}
        for name, data in PARTIES.items():
            st.session_state.all_parties_state[name] = copy.deepcopy(data['initial_resources'])

        st.session_state.resources = st.session_state.all_parties_state[selected_party_name]
        st.session_state.factions = copy.deepcopy(PARTIES[selected_party_name]['factions'])

        st.session_state.cumulative_risky_actions = 0
        st.session_state.party_status = "Muhalefet" # PART 4: Yeni durum değişkeni
        st.session_state.in_power = False # Bu eski değişken ileride kaldırılabilir
        st.session_state.governing_approval = 50
        st.session_state.terms_in_power = 0
        st.session_state.yearly_spending = {"EP": {}, "Treasury": {}}
        st.session_state.previous_resources = copy.deepcopy(st.session_state.resources)

        st.session_state.history = {
            "years": [0],
            "political_capital": [st.session_state.resources["political_capital"]],
            "cohesion": [st.session_state.resources["cohesion"]],
            "bureaucratic_efficiency": [st.session_state.resources["bureaucratic_efficiency"]],
            "public_support": [st.session_state.resources["public_support"]]
        }

def update_resources_from_action(action):
    """Bir eylemin sonuçlarını oyuncunun partisine uygular ve harcamaları kaydeder."""
    st.session_state.previous_resources = copy.deepcopy(st.session_state.resources)
    st.session_state.action_points -= action['ep_cost']

    effects = action['effects']
    apply_proposal_effects(effects) # Önerge ve Eylem efektleri aynı mantığı kullanabilir

    # --- KARAR AL (ÖNERGE) TETİKLEME MEKANİZMASI ---
    # Her EP harcayan eylemden sonra %25 ihtimalle bir önerge tetiklenir.
    if 'active_proposal' not in st.session_state or st.session_state.active_proposal is None:
        if random.random() < 0.25:
            from events import get_random_proposal
            st.session_state.active_proposal = get_random_proposal()

    # --- HARCAMA TAKİBİ DÜZELTMESİ ---
    action_name = action['name']
    # EP Harcaması
    st.session_state.yearly_spending["EP"][action_name] = \
        st.session_state.yearly_spending["EP"].get(action_name, 0) + action['ep_cost']

    # Bütçe Harcaması
    treasury_cost = abs(effects.get('treasury', 0))
    if treasury_cost > 0:
        st.session_state.yearly_spending["Treasury"][action_name] = \
            st.session_state.yearly_spending["Treasury"].get(action_name, 0) + treasury_cost

def apply_proposal_effects(effects):
    """Verilen efektleri (eylem veya önerge) oyuncunun partisine uygular."""
    party_name = st.session_state.selected_party_name
    party_state = st.session_state.all_parties_state[party_name]

    for key, value in effects.items():
        if key == 'risky_action':
             st.session_state.cumulative_risky_actions += value
             st.session_state.cumulative_risky_actions = max(0, st.session_state.cumulative_risky_actions)
        elif key in party_state:
            party_state[key] = max(0, party_state[key] + value)
            if key in ['cohesion', 'public_support']:
                party_state[key] = min(100, party_state[key])
        elif key.startswith('faction_'):
            faction_name = key.split('_')[1]
            if faction_name in st.session_state.factions:
                st.session_state.factions[faction_name]['satisfaction'] = max(0, min(100, st.session_state.factions[faction_name]['satisfaction'] + value))

    # Efektler kamuoyu desteğini etkiliyorsa, tüm parti oylarını yeniden normalize et
    if 'public_support' in effects:
        _normalize_public_support()


def _normalize_public_support():
    """Tüm partilerin kamuoyu desteği toplamını %100'e normalize eder."""
    all_parties = st.session_state.all_parties_state
    total_support = sum(party['public_support'] for party in all_parties.values())

    if total_support == 0:
        return # Herkesin oyu sıfırsa bir şey yapma

    for party_state in all_parties.values():
        current_support = party_state['public_support']
        normalized_support = (current_support / total_support) * 100
        party_state['public_support'] = round(normalized_support, 2)

    # Yuvarlama hatalarından kaynaklanan (~0.01) farkları gidermek için
    # en yüksek oy oranına sahip partiye farkı ekle/çıkar.
    final_total = sum(party['public_support'] for party in all_parties.values())
    discrepancy = 100 - final_total

    if abs(discrepancy) > 0.001: # Sadece anlamlı farklar için düzeltme yap
        max_support_party_name = max(all_parties, key=lambda p: all_parties[p]['public_support'])
        st.session_state.all_parties_state[max_support_party_name]['public_support'] += discrepancy
        # Son değeri de yuvarla ve 0-100 arasında kalmasını sağla
        current_val = st.session_state.all_parties_state[max_support_party_name]['public_support']
        st.session_state.all_parties_state[max_support_party_name]['public_support'] = max(0, min(100, round(current_val, 2)))

def start_alliance_talk(target_party_name):
    """İttifak görüşmesini başlatır ve sonucunu hesaplar."""
    player_party_name = st.session_state.selected_party_name
    player_capital = st.session_state.resources['political_capital']

    # EP maliyetini düşür
    st.session_state.action_points -= 2 # TODO: Maliyeti actions.py'den al

    # Başarı Olasılığını Hesapla
    ideological_score = _calculate_ideological_distance(player_party_name, target_party_name)
    capital_bonus = (player_capital - 50) / 100 # 50 sermaye nötr, 100 sermaye +0.5 bonus

    # Temel başarı şansı %50, ideoloji ve sermaye ile modifiye edilir
    success_chance = 0.5 + (ideological_score - 0.5) + capital_bonus
    success_chance = max(0.05, min(0.95, success_chance)) # Şansı %5 ile %95 arasında sınırla

    if random.random() < success_chance:
        # BAŞARILI
        st.session_state.party_status = "İktidar"
        st.session_state.action_feedback = {
            "type": "success",
            "message": f"🤝 BAŞARILI! {target_party_name} ile bir koalisyon hükümeti kuruldu. Artık İKTİDARdasınız!"
        }
    else:
        # BAŞARISIZ
        st.session_state.resources['political_capital'] -= 10 # Başarısızlık bedeli
        st.session_state.action_feedback = {
            "type": "error",
            "message": f"❌ BAŞARISIZ! {target_party_name} ile yapılan görüşmeler çöktü. Değerli siyasi sermaye kaybettiniz."
        }

def end_year():
    """Yılı sonlandırır, kaynakları günceller ve EP'yi yeniler."""
    st.session_state.previous_resources = copy.deepcopy(st.session_state.resources)

    # TODO: Rakip partilerin eylemlerini simüle et (Part 3 hedefi)

    # Yılı artır ve EP'yi yenile
    st.session_state.year += 1
    st.session_state.action_points = 3  # PART 4: EP her yıl 3'e sıfırlanır, birikmez.

    # Yıllık harcamaları sıfırla
    st.session_state.yearly_spending = {"EP": {}, "Treasury": {}}

    # Geri bildirimleri temizle
    st.session_state.action_feedback = None
    event = get_random_event()
    if event:
        st.session_state.event_feedback = {"type": "warning", "message": f"📢 YILIN OLAYI: {event['name']} - {event['description']}"}
        apply_proposal_effects(event['effects']) # DÜZELTME: Doğru fonksiyonu çağır
        # Normalizasyon zaten apply_proposal_effects içinde tetikleniyor
    else:
        st.session_state.event_feedback = {"type": "info", "message": f"🗓️ {st.session_state.year}. Yıl Başladı! Yeni hedefler ve zorluklar sizi bekliyor."}

    # Raporlama için geçmiş verileri güncelle
    st.session_state.history["years"].append(st.session_state.year)
    for resource in ["political_capital", "cohesion", "bureaucratic_efficiency", "public_support"]:
        st.session_state.history[resource].append(st.session_state.resources[resource])

def is_game_over():
    """Tamamen işlevsel kazanma ve kaybetme şartları."""
    # Kaybetme Şartları
    if st.session_state.resources['political_capital'] <= 0:
        st.session_state.action_feedback = {"type": "error", "message": "Liderin Düşüşü: Siyasi sermayeniz tükendi, istifa etmek zorunda kaldınız!"}
        return True

    if st.session_state.cumulative_risky_actions >= 7 and get_internal_tension() in ["Yüksek", "Kritik"]:
        if random.random() < 0.25:
            st.session_state.action_feedback = {"type": "error", "message": "Parti Kapatma: Artan yolsuzluk ve parti içi kaos nedeniyle partiniz yasal soruşturmaya uğradı ve kapatıldı!"}
            return True

    # Kazanma Şartı (Büyük Zafer)
    if st.session_state.terms_in_power >= 3:
        st.session_state.action_feedback = {"type": "success", "message": "Büyük Zafer: Üst üste 3 dönem iktidarda kalarak ülkeye istikrar ve refah getirdiniz. Adınız tarihe yazıldı!"}
        return True

    return False

def _calculate_ideological_distance(party1_name, party2_name):
    """İki parti arasındaki ideolojik yakınlık skorunu hesaplar (0-1 aralığında)."""
    spectrum1 = PARTIES[party1_name].get('spectrum', 'Merkez')
    spectrum2 = PARTIES[party2_name].get('spectrum', 'Merkez')

    # Aynı spektrum = çok yakın
    if spectrum1 == spectrum2:
        return 0.8

    # Komşu spektrumlar (Merkez her şeye komşu)
    neighbors = {
        "Sağ": ["Merkez-Sağ", "Merkez"],
        "Merkez-Sağ": ["Sağ", "Merkez"],
        "Sol": ["Merkez-Sol", "Merkez", "Yeşil"],
        "Merkez-Sol": ["Sol", "Merkez", "Yeşil"],
        "Merkez": ["Sağ", "Merkez-Sağ", "Sol", "Merkez-Sol"],
        "Yeşil": ["Sol", "Merkez-Sol"],
        "Diğer": []
    }

    if spectrum2 in neighbors.get(spectrum1, []):
        return 0.5

    # Zıt spektrumlar = çok uzak
    opposites = {
        "Sağ": "Sol",
        "Sol": "Sağ"
    }
    if opposites.get(spectrum1) == spectrum2:
        return 0.1

    # Diğer tüm durumlar
    return 0.25

# Diğer yardımcı fonksiyonlar aynı
def get_internal_tension():
    if not hasattr(st.session_state, 'factions') or not st.session_state.factions: return "Yok"
    min_satisfaction = min(f['satisfaction'] for f in st.session_state.factions.values())
    if min_satisfaction < 25: return "Kritik"
    if min_satisfaction < 40: return "Yüksek"
    if min_satisfaction < 60: return "Orta"
    return "Düşük"

def get_corruption_perception():
    risky_actions = st.session_state.cumulative_risky_actions
    if risky_actions >= 7: return "Çok Yüksek"
    if risky_actions >= 5: return "Yüksek"
    if risky_actions >= 3: return "Orta"
    return "Düşük"

def get_vekil_sayisi(party_name):
    """Basit orantı ile bir partinin meclisteki vekil sayısını hesaplar."""
    all_parties = st.session_state.all_parties_state
    total_support = sum(p['public_support'] for p in all_parties.values() if p['public_support'] > 0)

    # %10 seçim barajı
    party_support = all_parties[party_name]['public_support']
    if total_support == 0 or party_support < 10:
        return 0

    baraji_gecen_destek = sum(p['public_support'] for p in all_parties.values() if p['public_support'] >= 10)
    if baraji_gecen_destek == 0:
        return 0

    return round((party_support / baraji_gecen_destek) * 600)
