# -*- coding: utf-8 -*-

"""
tui.py: Metin Tabanlı Arayüz (TUI) fonksiyonlarını içerir.
Oyun durumunu konsola temiz, hizalı ve anlaşılır bir formatta basar.
"""

# Gerekli olabilecek modüller (ileride eklenebilir)
import os
from game_state import GameState # Fonksiyonların tip ipuçları için

def clear_screen():
    """Konsol ekranını temizler."""
    os.system('cls' if os.name == 'nt' else 'clear')

def format_change(value):
    """Değişim değerini formatlar (+, -, veya boş)."""
    if value > 0:
        return f"(+{value})"
    elif value < 0:
        return f"({value})"
    return ""

def display_turn_summary(game_state: GameState):
    """
    Her tur başında oyunun özetini konsola basar.

    Args:
        game_state (GameState): Anlık oyun durumu nesnesi.
    """
    clear_screen()

    # --- Başlık ---
    print("=" * 60)
    print(f"Partiler Savaşı | {game_state.selected_party_name} | Yıl: {((game_state.turn - 1) // 12) + 1}, Ay: {((game_state.turn - 1) % 12) + 1} (Tur: {game_state.turn}/48)")
    print("=" * 60)

    # --- Ana Kaynak Durumu ---
    print("\n--- STRATEJİK DURUM ---")

    # Değişimleri hesaplamak için bir önceki tur verilerini al
    history = game_state.history
    prev_pc = history["political_capital"][-2] if len(history["political_capital"]) > 1 else history["political_capital"][-1]
    prev_coh = history["cohesion"][-2] if len(history["cohesion"]) > 1 else history["cohesion"][-1]
    prev_be = history["bureaucratic_efficiency"][-2] if len(history["bureaucratic_efficiency"]) > 1 else history["bureaucratic_efficiency"][-1]
    prev_ps = history["public_support"][-2] if len(history["public_support"]) > 1 else history["public_support"][-1]

    pc_change = game_state.resources['political_capital'] - prev_pc
    coh_change = game_state.resources['cohesion'] - prev_coh
    be_change = game_state.resources['bureaucratic_efficiency'] - prev_be
    ps_change = game_state.resources['public_support'] - prev_ps

    print(f"{'Siyasi Sermaye':<25}: {game_state.resources['political_capital']:<5} {format_change(pc_change)}")
    print(f"{'İdeolojik Tutarlılık':<25}: {game_state.resources['cohesion']:<5} {format_change(coh_change)}")
    print(f"{'Bürokratik Verimlilik':<25}: {game_state.resources['bureaucratic_efficiency']:<5} {format_change(be_change)}")
    print(f"{'Kamuoyu Desteği':<25}: {game_state.resources['public_support']:<5} {format_change(ps_change)}")
    print(f"{'Hazine Bütçesi':<25}: {game_state.resources['treasury']:<10,}")

    # --- Meclis Durumu (Aşama 1 için statik) ---
    print("\n--- MECLİS DURUMU ---")
    total_mps = 550
    majority_threshold = 276
    player_mps = int(50 + (game_state.resources['public_support'] / 100) * 150) # Temsili hesaplama
    closest_rival_mps = 135 # Statik değer

    print(f"{'Sizin Vekil Sayınız':<25}: {player_mps}")
    print(f"{'En Yakın Rakip':<25}: {closest_rival_mps}")
    print(f"{'Çoğunluk Sınırı':<25}: {majority_threshold}")

    # --- Fraksiyon Memnuniyeti ---
    print("\n--- PARTİ İÇİ DİNAMİKLER ---")
    for name, data in game_state.factions.items():
        # Değişimleri göstermek için game_state'e fraksiyon geçmişi eklenmeli
        # Şimdilik sadece mevcut durumu gösteriyoruz.
        print(f"{name:<25}: %{data['satisfaction']}")

    # --- Risk Özetleri ---
    print("\n--- RİSK ÖZETLERİ ---")
    print(f"{'Parti İçi Gerilim':<25}: {game_state.get_internal_tension()}")
    print(f"{'Yolsuzluk Algısı':<25}: {game_state.get_corruption_perception()}")
    print("-" * 60)

def display_actions(actions):
    """
    Oyuncunun seçebileceği eylemleri listeler.
    """
    print("\n--- EYLEM SEÇENEKLERİ ---")
    for key, action in actions.items():
        print(f"[{key}] {action['name']}")
        print(f"    {action['description']}")

    print("-" * 60)

def get_player_choice(actions):
    """
    Oyuncudan geçerli bir eylem seçimi alır.
    """
    while True:
        choice = input("Lütfen bir eylem seçin (1-7): ")
        if choice in actions:
            return choice
        else:
            print("Geçersiz seçim. Lütfen listedeki numaralardan birini girin.")
