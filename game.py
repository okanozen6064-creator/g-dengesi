# -*- coding: utf-8 -*-

"""
game.py: Streamlit tabanlı ana uygulama dosyasını yönetir.
- Streamlit sayfa yapılandırmasını ayarlar.
- Oyunun durumuna göre (başlangıç, devam ediyor, bitti) doğru arayüz
  fonksiyonunu (ui.py'den) çağırır.
"""

import streamlit as st
import ui
import game_state

def main():
    """
    Ana Streamlit uygulama akışını yönetir.
    """
    # Sayfa yapılandırmasını ayarla (Part 3: Mobil Odaklı)
    st.set_page_config(layout="centered", page_title="Partiler Savaşı", initial_sidebar_state="collapsed")

    # Oyunun başlayıp başlamadığını session_state'den kontrol et
    if 'game_started' not in st.session_state:
        # Oyun başlamadıysa, parti seçim ekranını göster
        ui.display_party_selection()
    else:
        # Oyun başladıysa, oyunun bitip bitmediğini kontrol et
        if game_state.is_game_over():
            # Oyun bittiyse, ana oyun ekranını son bir kez göster
            # (kaybetme/kazanma mesajı burada gösterilecek)
            ui.display_main_game_screen()
            st.balloons()
            st.title("OYUN BİTTİ!")
            # Geri bildirim mesajı zaten is_game_over içinde ayarlanıyor.
        else:
            # Oyun devam ediyorsa, ana oyun ekranını göster
            ui.display_main_game_screen()

if __name__ == "__main__":
    main()
