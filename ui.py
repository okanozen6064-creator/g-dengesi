# -*- coding: utf-8 -*-

"""
ui.py: Streamlit tabanlı kullanıcı arayüzü bileşenlerini içerir.
Bu modül, oyunun web arayüzünü oluşturan tüm görsel elementleri
(sidebar, metrikler, butonlar, grafikler) yönetir.
"""

import streamlit as st
from parties import PARTIES
from actions import ACTIONS
import game_state
import reports

def display_sidebar():
    """
    Kenar çubuğunu (sidebar) oluşturur ve anlık kaynak durumunu gösterir.
    st.metric kullanarak kaynaklardaki değişimi görselleştirir.
    """
    with st.sidebar:
        st.header(f"Tur: {st.session_state.turn}/48")
        st.subheader(f"{st.session_state.selected_party_name}")

        st.divider()

        prev = st.session_state.previous_resources
        curr = st.session_state.resources

        pc_delta = curr['political_capital'] - prev['political_capital']
        coh_delta = curr['cohesion'] - prev['cohesion']
        be_delta = curr['bureaucratic_efficiency'] - prev['bureaucratic_efficiency']
        ps_delta = curr['public_support'] - prev['public_support']
        tr_delta = curr['treasury'] - prev['treasury']

        st.metric(label="Siyasi Sermaye", value=curr['political_capital'], delta=pc_delta)
        st.metric(label="İdeolojik Tutarlılık", value=curr['cohesion'], delta=coh_delta)
        st.metric(label="Bürokratik Verimlilik", value=curr['bureaucratic_efficiency'], delta=be_delta)
        st.metric(label="Kamuoyu Desteği", value=curr['public_support'], delta=ps_delta)
        st.metric(label="Hazine Bütçesi", value=f"{curr['treasury']:,}", delta=f"{tr_delta:,}")

def display_risk_panel():
    """
    Türetilmiş risk metriklerini (Gerilim ve Yolsuzluk) gösteren paneli oluşturur.
    """
    st.subheader("Risk Paneli")
    col1, col2 = st.columns(2)

    with col1:
        tension_level = game_state.get_internal_tension()
        st.metric(label="Parti İçi Gerilim", value=tension_level)

    with col2:
        corruption_level = game_state.get_corruption_perception()
        st.metric(label="Yolsuzluk Algısı", value=corruption_level)

def display_faction_satisfaction():
    """
    Fraksiyon memnuniyetlerini ilerleme çubukları ile gösterir.
    """
    st.subheader("Parti İçi Gruplar")
    factions = st.session_state.factions
    for name, data in factions.items():
        satisfaction = data['satisfaction']
        st.write(f"**{name}**")
        st.progress(satisfaction, text=f"{satisfaction}%")

def display_main_game_screen():
    """
    Oyunun ana ekranını (risk paneli, fraksiyonlar, eylemler, raporlar) oluşturur.
    """
    display_sidebar()
    st.title("Partiler Savaşı - Yönetim Paneli")

    if st.session_state.action_feedback:
        feedback = st.session_state.action_feedback
        if feedback["type"] == "success": st.success(feedback["message"])
        elif feedback["type"] == "info": st.info(feedback["message"])
        elif feedback["type"] == "warning": st.warning(feedback["message"])
        elif feedback["type"] == "error": st.error(feedback["message"])

    display_risk_panel()
    st.divider()
    display_faction_satisfaction()
    st.divider()

    st.subheader("Eylem Seçenekleri")
    cols = st.columns(3)
    action_keys = list(ACTIONS.keys())

    for i, key in enumerate(action_keys):
        action = ACTIONS[key]
        with cols[i % 3]:
            if st.button(action['name'], key=f"action_{key}"):
                st.session_state.action_feedback = None

                game_state.update_resources(action['effects'])
                st.session_state.action_feedback = {"type": "info", "message": f"'{action['name']}' eylemi gerçekleştirildi."}
                game_state.end_turn()
                st.rerun()

            cost = action['effects'].get('treasury', 0)
            pc_cost = action['effects'].get('political_capital', 0)
            st.caption(f"Maliyet: {abs(cost):,} | Sermaye: {pc_cost}")

    st.divider()

    st.header("Stratejik Raporlar")
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(reports.generate_strategic_health_report(), use_container_width=True)
    with col2:
        st.plotly_chart(reports.generate_regional_analysis_report(), use_container_width=True)

def display_party_selection():
    """
    Oyunun başlangıcındaki parti seçim ekranını oluşturur.
    """
    st.title("Partiler Savaşı'na Hoş Geldiniz!")
    st.subheader("Lütfen yönetmek istediğiniz partiyi seçin:")

    party_list = list(PARTIES.keys())
    for party_name in party_list:
        if st.button(f"{party_name} ({PARTIES[party_name]['ideology']})", key=party_name):
            game_state.initialize_game_state(party_name)
            st.rerun()
