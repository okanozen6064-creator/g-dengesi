# -*- coding: utf-8 -*-
"""
ui.py: Streamlit tabanlı kullanıcı arayüzü bileşenlerini içerir.
Part 3: Mobil odaklı, sekmeli ve estetik olarak zenginleştirilmiş arayüz.
"""

import streamlit as st
from parties import PARTIES
import game_state

# --- Helper Functions ---

def _calculate_vekil_sayisi(party_name):
    """Basit orantı ile bir partinin meclisteki vekil sayısını hesaplar."""
    # TODO: Seçim barajı gibi daha karmaşık mekanikler eklenebilir.
    all_parties = st.session_state.all_parties_state
    total_support = sum(p['public_support'] for p in all_parties.values())
    if total_support == 0:
        return 0
    party_support = all_parties[party_name]['public_support']
    return round((party_support / total_support) * 600) # 600 vekil varsayımı

# --- UI Component Functions ---

def _display_header():
    """Lider/Parti durum çubuğunu (üst kısım) oluşturur."""
    party_name = st.session_state.selected_party_name
    resources = st.session_state.resources

    col1, col2 = st.columns([1, 4])

    with col1:
        st.markdown(f"<p style='font-size: 80px; text-align: center;'>{PARTIES[party_name]['emoji']}</p>", unsafe_allow_html=True)

    with col2:
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            st.metric(label="💰 Hazine Bütçesi", value=f"{resources['treasury']:,}")
            st.metric(label="👑 Siyasi Sermaye", value=resources['political_capital'])
        with sub_col2:
            st.metric(label="📈 Kamuoyu Desteği", value=f"{resources['public_support']:.2f}%")
            st.metric(label="🏛️ Meclis Sandalyesi", value=_calculate_vekil_sayisi(party_name))

def _display_feedback_area():
    """Eylem ve olay geri bildirimlerini gösterir."""
    if st.session_state.get('action_feedback'):
        feedback = st.session_state.action_feedback
        if feedback['type'] == 'error':
            st.error(feedback['message'])
        else:
            st.success(feedback['message'])
        st.session_state.action_feedback = None # Geri bildirimi bir kez göster

    if st.session_state.get('event_feedback'):
        feedback = st.session_state.event_feedback
        st.warning(feedback['message'])
        st.session_state.event_feedback = None

def _display_main_game_screen_tabs():
    """Arayüzün ana sekmelerini ve içeriğini oluşturur."""

    # SEKMELER (İçerikleri sonraki adımlarda doldurulacak)
    tab_ulke, tab_politika, tab_propaganda, tab_meclis = st.tabs([
        "🌍 Ülke Durumu",
        "📜 Politikalar",
        "📢 Propaganda",
        "🏛️ Meclis"
    ])

    with tab_ulke:
        st.header("🌍 Ülke Genel Durum Raporları")
        st.write("Ülkenin siyasi ve bölgesel nabzını buradan takip edin.")

        from reports import generate_strategic_health_report, generate_regional_analysis_report, generate_spending_report

        # Raporları iki sütunlu bir düzende göster
        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(generate_regional_analysis_report(), use_container_width=True)

        with col2:
            st.subheader("Parti İçi Gruplar")
            if 'factions' in st.session_state and st.session_state.factions:
                for name, data in st.session_state.factions.items():
                    st.write(f"**{name}**")
                    st.progress(data['satisfaction'], text=f"{data['satisfaction']}% Memnuniyet")
            else:
                st.warning("Bu parti için fraksiyon bilgisi bulunmuyor.")

        st.divider()
        st.plotly_chart(generate_strategic_health_report(), use_container_width=True)
        st.divider()

        st.subheader("Yıllık Harcama Dökümü")
        if any(st.session_state.yearly_spending["EP"]): # Harcama yapıldıysa
            fig_ep, fig_treasury = generate_spending_report()
            col1_spend, col2_spend = st.columns(2)
            with col1_spend: st.plotly_chart(fig_ep, use_container_width=True)
            with col2_spend: st.plotly_chart(fig_treasury, use_container_width=True)
        else:
            st.info("Bu yıl henüz bir harcama yapılmadı.")

    with tab_politika:
        st.header("📜 Yeni Politikalar Geliştir")
        st.write("Kaynaklarınızı ve Eylem Puanınızı (EP) kullanarak partinizin geleceğini şekillendirecek kararlar alın.")

        from actions import POLITIKA_ACTIONS
        ep = st.session_state.action_points

        # Eylemleri 2'li sütunlar halinde göster
        cols = st.columns(2)
        for i, (key, action) in enumerate(POLITIKA_ACTIONS.items()):
            with cols[i % 2]:
                with st.container(border=True):
                    st.subheader(action['name'])
                    st.caption(action['description'])

                    is_disabled = ep < action['ep_cost'] or st.session_state.resources['treasury'] < abs(action['effects'].get('treasury', 0))
                    if st.button("Uygula", key=f"action_{key}", disabled=is_disabled, use_container_width=True):
                        game_state.update_resources_from_action(action)
                        st.session_state.action_feedback = {"type": "info", "message": f"'{action['name']}' eylemi başarıyla uygulandı."}
                        st.rerun()

                    cost_str = f"**EP Maliyeti:** {action['ep_cost']}"
                    treasury_effect = action['effects'].get('treasury', 0)
                    if treasury_effect != 0:
                        cost_str += f" | **Bütçe:** {abs(treasury_effect):,}"
                    st.markdown(cost_str)

    with tab_propaganda:
        st.header("📢 Algı Yönetimi ve Propaganda")
        st.write("Kamuoyu desteğini artırmak ve rakiplerinizi zayıflatmak için çeşitli propaganda taktikleri kullanın.")

        from actions import PROPAGANDA_ACTIONS
        ep = st.session_state.action_points

        # Eylemleri 2'li sütunlar halinde göster
        cols = st.columns(2)
        for i, (key, action) in enumerate(PROPAGANDA_ACTIONS.items()):
            with cols[i % 2]:
                with st.container(border=True):
                    st.subheader(action['name'])
                    st.caption(action['description'])

                    is_disabled = ep < action['ep_cost'] or st.session_state.resources['treasury'] < abs(action['effects'].get('treasury', 0))
                    if st.button("Başlat", key=f"action_{key}", disabled=is_disabled, use_container_width=True):
                        game_state.update_resources_from_action(action)
                        st.session_state.action_feedback = {"type": "info", "message": f"'{action['name']}' propagandası başarıyla başlatıldı."}
                        st.rerun()

                    cost_str = f"**EP Maliyeti:** {action['ep_cost']}"
                    treasury_effect = action['effects'].get('treasury', 0)
                    if treasury_effect != 0:
                        cost_str += f" | **Bütçe:** {abs(treasury_effect):,}"
                    st.markdown(cost_str)

    with tab_meclis:
        st.header("🏛️ Meclis ve Ulusal Siyaset")
        st.write("Meclis'teki sandalye dağılımını ve rakip partilerin güncel durumunu takip edin.")

        # Ulusal Siyaset Tablosu
        import pandas as pd

        parties_data = []
        all_parties = st.session_state.all_parties_state

        # Oyuncunun partisi dahil tüm partileri işle
        for name, data in all_parties.items():
            parties_data.append({
                "Parti": f"{PARTIES[name]['emoji']} {name}",
                "Kamuoyu Desteği (%)": f"{data['public_support']:.2f}",
                "🏛️ Vekil Sayısı": _calculate_vekil_sayisi(name),
                "💰 Hazine Durumu": f"{data['treasury']:,}"
            })

        df = pd.DataFrame(parties_data).set_index("Parti")

        # Oyuncunun partisini vurgulamak için stil fonksiyonu
        def highlight_player_party(row):
            player_party_name = f"{PARTIES[st.session_state.selected_party_name]['emoji']} {st.session_state.selected_party_name}"
            return ['background-color: #4A4E5A' if row.name == player_party_name else '' for _ in row]

        st.dataframe(df.style.apply(highlight_player_party, axis=1), use_container_width=True)

def _display_action_buttons():
    """'Yılı Bitir' butonunu oluşturur."""
    st.divider()
    ep = st.session_state.action_points
    if st.button(f"🗓️ Yılı Bitir ({ep} EP Kaldı)", use_container_width=True, type="primary"):
        game_state.end_year()
        st.session_state.active_proposal = None # Yeni yıla geçerken önergeyi temizle
        st.rerun()

def _display_proposal_modal():
    """Aktif önergeyi (varsa) bir modal içinde gösterir ve kararları işler."""
    proposal = st.session_state.active_proposal
    with st.container(border=True):
        st.subheader(f"🚨 GÜNDEM: {proposal['name']}")
        st.write(proposal['description'])

        cols = st.columns(len(proposal['choices']))
        for i, (choice, effects) in enumerate(proposal['choices'].items()):
            with cols[i]:
                if st.button(choice, key=f"choice_{choice}", use_container_width=True):
                    game_state.apply_proposal_effects(effects)
                    st.session_state.action_feedback = {"type": "info", "message": f"'{proposal['name']}' önergesine '{choice}' yanıtını verdiniz."}
                    st.session_state.active_proposal = None # Önergeyi temizle
                    st.rerun()

# --- Main Screen Function ---

def display_main_game_screen():
    """Oyunun ana ekranını yeni şemaya göre oluşturur."""
    _display_header()
    st.divider()
    _display_feedback_area()

    # Eğer aktif bir önerge varsa, sekmeleri gösterme, sadece önergeyi göster
    if st.session_state.get('active_proposal'):
        _display_proposal_modal()
    else:
        # Ana içerik ve sekmeler
        _display_main_game_screen_tabs()

    # Alt eylem butonları (Yılı Bitir)
    _display_action_buttons()

def display_party_selection():
    """Parti seçim ekranını oluşturur."""
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
