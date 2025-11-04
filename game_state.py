# -*- coding: utf-8 -*-

"""
game_state.py: Oyunun anlık durumunu yöneten GameState sınıfını içerir.
Bu sınıf, oyuncunun seçimlerine ve eylemlerine göre değişen tüm dinamik
verileri yönetir ve saklar.
"""

import copy
from parties import PARTIES

class GameState:
    """
    Oyunun mevcut durumunu yönetir.
    - Tur sayısı
    - Oyuncunun partisinin anlık kaynakları
    - Fraksiyon memnuniyetleri
    - Raporlama için geçmiş veri takibi
    """
    def __init__(self, selected_party_name):
        """
        GameState nesnesini seçilen partiyle başlatır.

        Args:
            selected_party_name (str): Oyuncunun seçtiği partinin adı.
        """
        if selected_party_name not in PARTIES:
            raise ValueError(f"Geçersiz parti adı: {selected_party_name}")

        self.selected_party_name = selected_party_name
        self.party_data = copy.deepcopy(PARTIES[selected_party_name])

        # Dinamik oyun durumu değişkenleri
        self.turn = 1
        self.resources = self.party_data['initial_resources']
        self.factions = self.party_data['factions']
        self.cumulative_risky_actions = 0 # Yolsuzluk Algısı için

        # Raporlama için geçmiş verileri sakla (ilk değerler dahil)
        self.history = {
            "turns": [0],
            "political_capital": [self.resources["political_capital"]],
            "cohesion": [self.resources["cohesion"]],
            "bureaucratic_efficiency": [self.resources["bureaucratic_efficiency"]],
            "public_support": [self.resources["public_support"]]
        }

    def update_resources(self, effects):
        """
        Bir eylemin sonuçlarını mevcut kaynaklara ve memnuniyetlere uygular.

        Args:
            effects (dict): Kaynaklara ve fraksiyonlara uygulanacak değişiklikler.
                            Örn: {'political_capital': -5, 'treasury': -10000,
                                  'factions': {'Şahinler': 5, 'Merkezciler': -5}}
        """
        for key, value in effects.items():
            if key in self.resources:
                # Hazine hariç kaynakları 0-100 aralığında tut
                if key != 'treasury':
                    self.resources[key] = max(0, min(100, self.resources[key] + value))
                else:
                    self.resources[key] += value
            elif key == 'factions':
                for faction_name, satisfaction_change in value.items():
                    if faction_name in self.factions:
                        self.factions[faction_name]['satisfaction'] = max(0, min(100,
                            self.factions[faction_name]['satisfaction'] + satisfaction_change))
            elif key == 'risky_action':
                self.cumulative_risky_actions += value


    def get_internal_tension(self):
        """
        Fraksiyon memnuniyetlerine göre Parti İçi Gerilim seviyesini hesaplar.

        Returns:
            str: "Düşük", "Orta", "Yüksek" veya "Kritik".
        """
        if not self.factions:
            return "Yok"

        min_satisfaction = min(f['satisfaction'] for f in self.factions.values())

        if min_satisfaction < 25:
            return "Kritik"
        if min_satisfaction < 40:
            return "Yüksek"
        if min_satisfaction < 60:
            return "Orta"
        return "Düşük"

    def get_corruption_perception(self):
        """
        Riskli eylem sayısına göre Yolsuzluk Algısı seviyesini hesaplar.

        Returns:
            str: "Düşük", "Orta", "Yüksek".
        """
        if self.cumulative_risky_actions >= 5:
            return "Çok Yüksek"
        if self.cumulative_risky_actions >= 3:
            return "Yüksek"
        if self.cumulative_risky_actions >= 1:
            return "Orta"
        return "Düşük"


    def end_turn(self):
        """
        Turu sonlandırır, tur sayacını artırır ve geçmiş verileri kaydeder.
        """
        self.turn += 1
        self.history["turns"].append(self.turn - 1)
        self.history["political_capital"].append(self.resources["political_capital"])
        self.history["cohesion"].append(self.resources["cohesion"])
        self.history["bureaucratic_efficiency"].append(self.resources["bureaucratic_efficiency"])
        self.history["public_support"].append(self.resources["public_support"])

    def is_game_over(self):
        """
        Oyunun bitip bitmediğini kontrol eder. (Aşama 1 için temel kontrol)

        Returns:
            bool: Oyun bittiyse True, aksi takdirde False.
        """
        if self.resources['political_capital'] <= 0:
            print("Siyasi Sermayeniz tükendi! Güven oylamasını kaybettiniz.")
            return True
        if self.resources['treasury'] < 0:
            print("Hazine iflas etti! Ülkeyi yönetemez durumdasınız.")
            return True
        if self.turn > 48:
            print("4 yıllık yönetim süresi sona erdi. Seçim zamanı!")
            return True
        return False
