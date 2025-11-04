# -*- coding: utf-8 -*-

"""
game_state.py: Streamlit'in session_state'ini kullanarak oyun durumunu yönetir.
Bu modül, sınıf tabanlı bir yapı yerine, doğrudan st.session_state üzerinde
çalışan fonksiyonlar içerir. Bu, Streamlit'in yeniden çalışma döngüsünde
oyun durumunun korunmasını sağlar.
"""

import streamlit as st
import copy
from parties import PARTIES

def initialize_game_state(selected_party_name):
    """
    Oyun durumunu st.session_state içinde ilk kez başlatır.
    Bu fonksiyon sadece oyunun en başında bir kez çağrılmalıdır.
    """
    if 'game_started' not in st.session_state:
        if selected_party_name not in PARTIES:
            st.error(f"Geçersiz parti adı: {selected_party_name}")
            return

        party_data = copy.deepcopy(PARTIES[selected_party_name])

        st.session_state.game_started = True
        st.session_state.selected_party_name = selected_party_name
        st.session_state.turn = 1
        st.session_state.resources = party_data['initial_resources']
        st.session_state.factions = party_data['factions']
        st.session_state.cumulative_risky_actions = 0
        st.session_state.action_feedback = None

        st.session_state.previous_resources = copy.deepcopy(st.session_state.resources)

        st.session_state.history = {
            "turns": [0],
            "political_capital": [st.session_state.resources["political_capital"]],
            "cohesion": [st.session_state.resources["cohesion"]],
            "bureaucratic_efficiency": [st.session_state.resources["bureaucratic_efficiency"]],
            "public_support": [st.session_state.resources["public_support"]]
        }

def update_resources(effects):
    """
    Bir eylemin sonuçlarını mevcut kaynaklara ve memnuniyetlere uygular.
    Doğrudan st.session_state üzerinde çalışır.
    """
    st.session_state.previous_resources = copy.deepcopy(st.session_state.resources)

    for key, value in effects.items():
        if key in st.session_state.resources:
            if key != 'treasury':
                st.session_state.resources[key] = max(0, min(100, st.session_state.resources[key] + value))
            else:
                st.session_state.resources[key] += value
        elif key == 'factions':
            for faction_name, satisfaction_change in value.items():
                if faction_name in st.session_state.factions:
                    st.session_state.factions[faction_name]['satisfaction'] = max(0, min(100,
                        st.session_state.factions[faction_name]['satisfaction'] + satisfaction_change))
        elif key == 'risky_action':
            st.session_state.cumulative_risky_actions += value

def get_internal_tension():
    """Fraksiyon memnuniyetlerine göre Parti İçi Gerilim seviyesini hesaplar."""
    if not st.session_state.factions: return "Yok"
    min_satisfaction = min(f['satisfaction'] for f in st.session_state.factions.values())
    if min_satisfaction < 25: return "Kritik"
    if min_satisfaction < 40: return "Yüksek"
    if min_satisfaction < 60: return "Orta"
    return "Düşük"

def get_corruption_perception():
    """Riskli eylem sayısına göre Yolsuzluk Algısı seviyesini hesaplar."""
    risky_actions = st.session_state.cumulative_risky_actions
    if risky_actions >= 5: return "Çok Yüksek"
    if risky_actions >= 3: return "Yüksek"
    if risky_actions >= 1: return "Orta"
    return "Düşük"

def end_turn():
    """Turu sonlandırır, tur sayacını artırır ve geçmiş verileri kaydeder."""
    st.session_state.turn += 1

    history = st.session_state.history
    history["turns"].append(st.session_state.turn - 1)
    history["political_capital"].append(st.session_state.resources["political_capital"])
    history["cohesion"].append(st.session_state.resources["cohesion"])
    history["bureaucratic_efficiency"].append(st.session_state.resources["bureaucratic_efficiency"])
    history["public_support"].append(st.session_state.resources["public_support"])

def is_game_over():
    """Oyunun bitip bitmediğini kontrol eder."""
    if st.session_state.resources['political_capital'] <= 0:
        st.session_state.action_feedback = {"type": "error", "message": "Siyasi Sermayeniz tükendi! Güven oylamasını kaybettiniz."}
        return True
    if st.session_state.resources['treasury'] < 0:
        st.session_state.action_feedback = {"type": "error", "message": "Hazine iflas etti! Ülkeyi yönetemez durumdasınız."}
        return True
    if st.session_state.turn > 48:
        st.session_state.action_feedback = {"type": "success", "message": "4 yıllık yönetim süresi sona erdi. Seçim zamanı!"}
        return True
    return False
