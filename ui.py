# -*- coding: utf-8 -*-

"""
ui.py: Streamlit tabanlı kullanıcı arayüzü bileşenlerini içerir.
İktidar Döngüsü mekaniklerini ve TÜM tamamlanmış UI bileşenlerini destekler.
"""

import streamlit as st
import pandas as pd
from parties import PARTIES
from actions import ACTIONS
import game_state
import reports

def display_sidebar():
    """Kenar çubuğunu oluşturur ve anlık kaynak durumunu gösterir."""
    with st.sidebar:
        st.header(f"Yıl: {st.session_state.year}")
        st.metric(label="Eylem Puanı (EP)", value=f"{st.session_state.action_points} / 5")
        st.divider()
        st.subheader(f"{st.session_state.selected_party_name}")

        prev = st.session_state.previous_resources
        curr = st.session_state.resources

        # ... (delta hesaplamaları)

        st.metric(label="Siyasi Sermaye", value=curr['political_capital'], delta=curr['political_capital'] - prev['political_capital'])
        st.metric(label="İdeolojik Tutarlılık", value=curr['cohesion'], delta=curr['cohesion'] - prev['cohesion'])
        st.metric(label="Bürokratik Verimlilik", value=curr['bureaucratic_efficiency'], delta=curr['bureaucratic_efficiency'] - prev['bureaucratic_efficiency'])
        st.metric(label="Kamuoyu Desteği", value=curr['public_support'], delta=curr['public_support'] - prev['public_support'])
        st.metric(label="Hazine Bütçesi", value=f"{curr['treasury']:,}", delta=f"{(curr['treasury'] - prev['treasury']):,}")

def display_national_politics():
    """Diğer partilerin dinamik durumunu gösteren tabloyu oluşturur."""
    st.subheader("Ulusal Siyaset Tablosu")
    parties_data = []
    for name, data in st.session_state.all_parties_state.items():
        parties_data.append({
            "Parti": name,
            "Kamuoyu Desteği (%)": data['public_support'],
            "Hazine Durumu": f"{data['treasury']:,}"
        })
    df = pd.DataFrame(parties_data).set_index("Parti")

    def highlight_player_party(s):
        return ['background-color: #3C4B64' if s.name == st.session_state.selected_party_name else '' for _ in s]

    st.dataframe(df.style.apply(highlight_player_party, axis=1), use_container_width=True)

def display_risk_panel():
    """Türetilmiş risk metriklerini gösterir."""
    st.subheader("Risk Paneli")
    col1, col2 = st.columns(2)
    with col1:
        tension = game_state.get_internal_tension()
        st.metric("Parti İçi Gerilim", tension)
    with col2:
        corruption = game_state.get_corruption_perception()
        st.metric("Yolsuzluk Algısı", corruption)

def display_faction_satisfaction():
    """Fraksiyon memnuniyetlerini ilerleme çubukları ile gösterir."""
    st.subheader("Parti İçi Gruplar")
    for name, data in st.session_state.factions.items():
        st.write(f"**{name}**")
        st.progress(data['satisfaction'], text=f"{data['satisfaction']}%")

def display_main_game_screen():
    """Oyunun ana ekranını oluşturur."""
    display_sidebar()
    st.title("Partiler Savaşı - Yönetim Paneli")

    # ... (geri bildirimler)

    display_risk_panel()
    st.divider()
    display_faction_satisfaction()
    st.divider()

    st.subheader("Eylem Seçenekleri")
    cols = st.columns(3)
    for i, (key, action) in enumerate(ACTIONS.items()):
        with cols[i % 3]:
            is_disabled = st.session_state.action_points < action['ep_cost']
            if st.button(action['name'], key=f"action_{key}", disabled=is_disabled, help=action['description']):
                game_state.update_resources_from_action(action)
                st.session_state.action_feedback = {"type": "info", "message": f"'{action['name']}' eylemi gerçekleştirildi."}
                st.rerun()
            st.caption(f"EP Maliyeti: {action['ep_cost']} | Bütçe: {abs(action['effects'].get('treasury', 0)):,}")

    st.divider()

    if st.session_state.action_points == 0:
        st.warning("Eylem Puanınız (EP) tükendi. Bir sonraki yıla geçmelisiniz.")

    if st.button("Yılı Bitir", type="primary", use_container_width=True):
        game_state.end_year()
        st.rerun()

    st.divider()
    display_national_politics()
    st.divider()

    st.header("Yıllık Faaliyet Raporları")
    if any(st.session_state.yearly_spending["EP"]): # Harcama yapıldıysa
        fig_ep, fig_treasury = reports.generate_spending_report()
        col1, col2 = st.columns(2)
        with col1: st.plotly_chart(fig_ep, use_container_width=True)
        with col2: st.plotly_chart(fig_treasury, use_container_width=True)
    else:
        st.info("Bu yıl henüz bir harcama yapılmadı.")

    st.plotly_chart(reports.generate_strategic_health_report(), use_container_width=True)
    st.plotly_chart(reports.generate_regional_analysis_report(), use_container_width=True)

def display_party_selection():
    """Parti seçim ekranını oluşturur."""
    # ... (aynı)
    st.title("Partiler Savaşı")
    # ...
