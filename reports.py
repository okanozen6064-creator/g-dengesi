# -*- coding: utf-8 -*-

"""
reports.py: Matplotlib kullanarak görsel raporlar üretir.
Her tur sonunda oyun durumu hakkında üç farklı grafik oluşturur,
bunları ekranda gösterir ve /reports/ klasörüne kaydeder.
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from game_state import GameState
from parties import REGIONS

# Raporların kaydedileceği klasörün varlığını kontrol et
if not os.path.exists('reports'):
    os.makedirs('reports')

def generate_strategic_health_report(game_state: GameState):
    """
    Stratejik Sağlık Takibi: 4 temel kaynağın zaman içindeki değişimini gösteren çizgi grafik.
    """
    history = game_state.history
    turns = history['turns']

    plt.figure(figsize=(10, 6))
    plt.plot(turns, history['political_capital'], label='Siyasi Sermaye', marker='o')
    plt.plot(turns, history['cohesion'], label='İdeolojik Tutarlılık', marker='o')
    plt.plot(turns, history['bureaucratic_efficiency'], label='Bürokratik Verimlilik', marker='o')
    plt.plot(turns, history['public_support'], label='Kamuoyu Desteği', marker='o')

    plt.title('Stratejik Sağlık Takibi (Tur 0\'dan İtibaren)')
    plt.xlabel('Tur')
    plt.ylabel('Değer (0-100)')
    plt.legend()
    plt.grid(True)
    plt.xticks(range(0, game_state.turn, max(1, game_state.turn // 10)))
    plt.ylim(0, 100)

    filepath = f'reports/tur_{game_state.turn}_stratejik_saglik.png'
    plt.savefig(filepath)
    print(f"Stratejik Sağlık Raporu oluşturuldu: {filepath}")


def generate_regional_analysis_report(game_state: GameState):
    """
    Bölgesel Başarı Analizi: Bölgelerdeki oy oranı ile doğal çekimi karşılaştıran sütun grafik.
    """
    party_name = game_state.selected_party_name
    region_names = list(REGIONS.keys())
    natural_attraction = [REGIONS[r]['natural_attraction'][party_name] for r in region_names]

    current_vote_share = [na + (game_state.resources['public_support'] - 50) / 5 for na in natural_attraction]
    current_vote_share = [max(5, min(95, v)) for v in current_vote_share]

    x = np.arange(len(region_names))
    width = 0.35

    fig, ax = plt.subplots(figsize=(14, 7))
    rects1 = ax.bar(x - width/2, natural_attraction, width, label='Doğal Çekim')
    rects2 = ax.bar(x + width/2, current_vote_share, width, label='Mevcut Oy Oranı')

    ax.set_ylabel('Yüzde (%)')
    ax.set_title('Bölgesel Başarı Analizi')
    ax.set_xticks(x)
    ax.set_xticklabels(region_names, rotation=45, ha="right")
    ax.legend()
    ax.grid(axis='y', linestyle='--')
    plt.ylim(0, 100)
    fig.tight_layout()

    filepath = f'reports/tur_{game_state.turn}_bolgesel_analiz.png'
    plt.savefig(filepath)
    print(f"Bölgesel Analiz Raporu oluşturuldu: {filepath}")


def generate_social_dynamics_report(game_state: GameState):
    """
    Toplumsal Dinamikler: Ülke genelindeki hassasiyetleri gösteren pasta grafikleri.
    """
    avg_sensitivities = {
        'Göçmen Hass.': np.mean([r['sensitivities']['immigrant'] for r in REGIONS.values()]),
        'Gelir Eşitsizliği Alg.': np.mean([r['sensitivities']['inequality'] for r in REGIONS.values()]),
        'Kutuplaşma Sev.': np.mean([r['sensitivities']['polarization'] for r in REGIONS.values()])
    }

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Ülke Geneli Toplumsal Dinamikler', fontsize=16)

    for i, (label, size) in enumerate(avg_sensitivities.items()):
        ax = axes[i]
        ax.pie([size, 100-size], labels=[label, ''], autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
        ax.axis('equal')

    filepath = f'reports/tur_{game_state.turn}_toplumsal_dinamikler.png'
    plt.savefig(filepath)
    print(f"Toplumsal Dinamikler Raporu oluşturuldu: {filepath}")

def generate_all_reports(game_state: GameState):
    """
    Tüm raporları tek seferde oluşturur, kaydeder ve ekranda gösterir.
    """
    print("\n--- Raporlar Oluşturuluyor ---")
    generate_strategic_health_report(game_state)
    generate_regional_analysis_report(game_state)
    generate_social_dynamics_report(game_state)
    print("---------------------------------")
    # Tüm figürleri oluşturduktan sonra, hepsini aynı anda göster.
    # Kullanıcı pencereleri kapattığında oyun devam eder.
    print("\nRapor pencereleri açılıyor... (Devam etmek için pencereleri kapatın)")
    plt.show()
