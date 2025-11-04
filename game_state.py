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
        # ... (başlangıç kodunun çoğu aynı)
        st.session_state.game_started = True
        st.session_state.selected_party_name = selected_party_name
        st.session_state.year = 1
        st.session_state.action_points = 5

        st.session_state.action_feedback = None
        st.session_state.event_feedback = None

        st.session_state.all_parties_state = {}
        for name, data in PARTIES.items():
            st.session_state.all_parties_state[name] = copy.deepcopy(data['initial_resources'])

        st.session_state.resources = st.session_state.all_parties_state[selected_party_name]
        st.session_state.factions = copy.deepcopy(PARTIES[selected_party_name]['factions'])

        st.session_state.cumulative_risky_actions = 0
        st.session_state.in_power = False
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
    _apply_effects(effects, st.session_state.selected_party_name)

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

def _apply_effects(effects, party_name):
    # ... (öncekiyle aynı)
    party_state = st.session_state.all_parties_state[party_name]
    # ...

def end_year():
    # ... (öncekiyle aynı)
    st.session_state.year += 1
    # ...

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
