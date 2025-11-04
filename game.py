# -*- coding: utf-8 -*-

"""
game.py: Ana oyun döngüsünü yönetir.
- Parti seçimi
- Tur ilerlemesi
- Oyuncu eylemlerinin işlenmesi
- TUI ve Raporlama modüllerinin çağrılması
"""

from parties import PARTIES
from game_state import GameState
from actions import ACTIONS
import tui
import reports

def select_party():
    """Oyuncunun yöneteceği partiyi seçmesini sağlar."""
    tui.clear_screen()
    print("=" * 60)
    print("Partiler Savaşı'na Hoş Geldiniz!")
    print("=" * 60)
    print("\nLütfen yönetmek istediğiniz partiyi seçin:\n")

    party_list = list(PARTIES.keys())
    for i, party_name in enumerate(party_list):
        print(f"[{i + 1}] {party_name} ({PARTIES[party_name]['ideology']})")

    print("-" * 60)

    while True:
        try:
            choice = int(input(f"Seçiminizi yapın (1-{len(party_list)}): "))
            if 1 <= choice <= len(party_list):
                return party_list[choice - 1]
            else:
                print("Lütfen listedeki numaralardan birini girin.")
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")

def main_game_loop():
    """Ana oyun döngüsünü başlatır ve yönetir."""

    # 1. Parti Seçimi
    selected_party = select_party()

    # 2. Oyun Durumunu Başlatma
    game = GameState(selected_party)

    # 3. Ana Döngü
    while not game.is_game_over():
        # Tur özeti
        tui.display_turn_summary(game)

        # Eylem Seçenekleri
        tui.display_actions(ACTIONS)

        # Oyuncu Kararı
        action_key = tui.get_player_choice(ACTIONS)
        chosen_action = ACTIONS[action_key]

        # Eylem Sonuçlarını Uygula
        print(f"\n'{chosen_action['name']}' eylemi gerçekleştiriliyor...")
        game.update_resources(chosen_action['effects'])

        # Tur Sonu Raporları Oluştur
        reports.generate_all_reports(game)

        # Turu Sonlandır
        game.end_turn()

        # Bir sonraki tura geçmeden önce kullanıcıdan input bekle
        input("\nTur sonlandı. Devam etmek için Enter'a basın...")

    # 4. Oyun Sonu
    tui.clear_screen()
    print("=" * 60)
    print("OYUN BİTTİ")
    print("=" * 60)
    # is_game_over() zaten kaybetme nedenini basıyor.
    print(f"\nToplam {game.turn - 1} tur oynadınız.")
    print("Nihai durum raporları 'reports' klasöründe bulunabilir.")


if __name__ == "__main__":
    try:
        main_game_loop()
    except KeyboardInterrupt:
        print("\nOyun isteğiniz üzerine kapatıldı.")
