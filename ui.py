# -*- coding: utf-8 -*-
"""
ui.py: Streamlit tabanlı kullanıcı arayüzü bileşenlerini içerir.
Part 4: Sabit, kaydırmasız Dashboard mimarisi.
"""

import streamlit as st
from parties import PARTIES
import game_state
from reports import generate_regional_analysis_report

# --- Panel İçerik Fonksiyonları ---

def _display_ulke_durumu_panel():
    """'Ülke Durumu' panelinin içeriğini oluşturur."""
    st.plotly_chart(generate_regional_analysis_report(), use_container_width=True)
    if 'factions' in st.session_state and st.session_state.factions:
        with st.container(border=True):
            for name, data in st.session_state.factions.items():
                st.progress(data['satisfaction'], text=f"{name}: {data['satisfaction']}% Memnuniyet")
    else:
        st.warning("Bu parti için fraksiyon bilgisi bulunmuyor.")

def _display_politika_panel():
    """'Politikalar' panelinin içeriğini oluşturur."""
    st.subheader("📜 Politikalar ve Stratejik Hamleler")
    status = st.session_state.party_status
    st.caption(f"Durum: **{status}**")

    from actions import GENEL_ACTIONS, MUHALEFET_ACTIONS, IKTIDAR_ACTIONS
    available_actions = GENEL_ACTIONS.copy()
    if status == "Muhalefet":
        available_actions.update(MUHALEFET_ACTIONS)
    elif status == "İktidar":
        available_actions.update(IKTIDAR_ACTIONS)

    ep = st.session_state.action_points

    # İttifak görüşmesi için özel arayüz
    if "MUH_ITTİFAK_GORUSMESI" in available_actions:
        action = available_actions.pop("MUH_ITTİFAK_GORUSMESI")
        with st.expander(f"🤝 {action['name']}", expanded=False):
            st.caption(action['description'])
            possible_allies = [p for p in PARTIES.keys() if p != st.session_state.selected_party_name]
            target_party = st.selectbox("Görüşülecek Partiyi Seçin:", possible_allies, key="alliance_target")

            is_disabled = ep < action['ep_cost']
            if st.button("Görüşmeyi Başlat", key="alliance_talk", disabled=is_disabled, use_container_width=True):
                game_state.start_alliance_talk(target_party)
                st.rerun()

    for key, action in available_actions.items():
        is_disabled = ep < action['ep_cost']
        button_text = f"{action['name']} ({action['ep_cost']} EP)"

        if st.button(button_text, key=f"action_{key}", disabled=is_disabled, use_container_width=True):
            game_state.update_resources_from_action(action)
            st.rerun()

def _display_propaganda_panel():
    """'Propaganda' panelinin içeriğini oluşturur."""
    st.subheader("📢 Propaganda Faaliyetleri")
    st.caption("Bu eylemler her durumda kullanılabilir.")
    from actions import GENEL_ACTIONS # Propaganda eylemleri genel eylemlerin içinde
    ep = st.session_state.action_points
    for key, action in GENEL_ACTIONS.items():
        # TODO: Sadece propaganda etiketli eylemleri filtrele
        is_disabled = ep < action['ep_cost']
        button_text = f"{action['name']} ({action['ep_cost']} EP)"
        if st.button(button_text, key=f"prop_action_{key}", disabled=is_disabled, use_container_width=True):
            game_state.update_resources_from_action(action)
            st.rerun()

def _display_meclis_panel():
    """'Meclis' panelinin içeriğini oluşturur."""
    st.subheader("🏛️ Meclis Gündemi ve Yasa Tasarıları")
    st.caption("Buradaki tasarıları oylamaya sunarak meclis gündemini belirleyebilirsiniz.")
    from events import PROPOSALS

    for i, proposal in enumerate(PROPOSALS):
        with st.expander(f"📜 {proposal['name']}"):
            st.write(proposal['description'])
            if st.button("Oylamaya Sun", key=f"vote_{i}", use_container_width=True):
                st.session_state.active_proposal = proposal
                st.rerun()

def _display_header():
    """Lider/Parti durum çubuğunu (üst kısım) oluşturur."""
    party_name = st.session_state.selected_party_name
    resources = st.session_state.resources
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"<h1 style='text-align: center; font-size: 5rem; margin-top: -1rem;'>{PARTIES[party_name]['emoji']}</h1>", unsafe_allow_html=True)
    with col2:
        sub_col1, sub_col2, sub_col3, sub_col4 = st.columns(4)
        sub_col1.metric("💰 Bütçe", f"{resources['treasury']:,}")
        sub_col2.metric("📈 Oy Oranı", f"{resources['public_support']:.1f}%")
        sub_col3.metric("👑 S. Sermaye", resources['political_capital'])
        sub_col4.metric("🏛️ Vekil", game_state.get_vekil_sayisi(party_name))

# --- Ana Dashboard Mimarisi ---

def display_main_game_screen():
    """Oyunun ana, sabitlenmiş dashboard ekranını oluşturur."""

    # --- ÜST PANEL (LİDER ÖZETİ) ---
    with st.container(height=150, border=False):
        _display_header()

    st.divider() # Üst panel ile orta panel arasına ayırıcı çizgi

    # --- ORTA PANEL (DİNAMİK İÇERİK) ---
    with st.container(height=450, border=True):
        active_panel = st.session_state.get('active_panel', 'Ülke Durumu')

        if active_panel == 'Ülke Durumu':
            _display_ulke_durumu_panel()
        elif active_panel == 'Politikalar':
            _display_politika_panel()
        elif active_panel == 'Propaganda':
            _display_propaganda_panel()
        elif active_panel == 'Meclis':
            _display_meclis_panel()

    # --- ALT PANEL (NAVİGASYON VE EYLEM) ---
    with st.container(height=200, border=False):
        # Navigasyon Butonları
        col1, col2, col3, col4 = st.columns(4)
        if col1.button("🌍 Ülke Durumu", use_container_width=True):
            st.session_state.active_panel = "Ülke Durumu"
            st.rerun()
        if col2.button("📜 Politikalar", use_container_width=True):
            st.session_state.active_panel = "Politikalar"
            st.rerun()
        if col3.button("📢 Propaganda", use_container_width=True):
            st.session_state.active_panel = "Propaganda"
            st.rerun()
        if col4.button("🏛️ Meclis", use_container_width=True):
            st.session_state.active_panel = "Meclis"
            st.rerun()

        st.empty() # Boşluk

        # Aksiyon Düğmeleri
        col1, col2 = st.columns(2)
        from events import get_random_proposal
        if col1.button("🚨 Karar Al", use_container_width=True):
            st.session_state.active_proposal = get_random_proposal()
            st.rerun()
        if col2.button(f"🗓️ Yılı Bitir ({st.session_state.action_points} EP Kaldı)", type="primary", use_container_width=True):
            game_state.end_year()
            st.rerun()

# Parti Seçim Ekranı (değişiklik yok)
def display_party_selection():
    st.title("Partiler Savaşı")
    st.subheader("Bir Parti Seçerek Oyuna Başlayın")
    cols = st.columns(4)
    party_names = list(PARTIES.keys())
    for i, party_name in enumerate(party_names):
        with cols[i % 4]:
            party_info = PARTIES[party_name]
            st.markdown(f"### {party_info['emoji']} {party_name}")
            st.caption(party_info['description'])
            if st.button(f"Olarak Başla", key=f"party_{party_name}", use_container_width=True):
                game_state.initialize_game_state(party_name)
                st.rerun()
