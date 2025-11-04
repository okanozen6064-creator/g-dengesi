# -*- coding: utf-8 -*-

"""
events.py: Oyun içinde tetiklenebilecek rastgele olayları içerir.
Her olay, bir başlık, açıklama metni ve oyun durumu üzerindeki
etkilerini içeren bir sözlük olarak tanımlanmıştır.
"""

import random

EVENTS = [
    {
        "name": "Ekonomik Canlanma",
        "get_description": lambda: (
            "Beklenmedik Büyüme Rakamları!",
            "Uluslararası piyasalardaki olumlu hava ve ülkedeki sanayi üretimindeki beklenmedik artış, "
            "ekonomide bir canlanma yarattı. Hazine'ye ek gelir aktarıldı. Bu fırsatı akıllıca "
            "kullanarak halkın refahını artırabilir veya parti gücünüzü pekiştirebilirsiniz."
        ),
        "effects": {
            "treasury": 50000,
            "public_support": 5
        },
        "type": "positive"
    },
    {
        "name": "Yolsuzluk Sızıntısı",
        "get_description": lambda: (
            "Basına Sızan Şok Belgeler!",
            "Partinizin üst düzey yöneticilerinden birinin adının karıştığı bir ihale skandalı, "
            "önde gelen bir gazeteci tarafından ortaya çıkarıldı. Belgeler, kamu kaynaklarının "
            "usulsüz kullanıldığını iddia ediyor. Bu sızıntı, partiye olan güveni sarstı ve "
            "liderlik otoritenizi ciddi şekilde zedeledi."
        ),
        "effects": {
            "political_capital": -15,
            "public_support": -10,
            "cohesion": -5
        },
        "type": "negative"
    },
    {
        "name": "Uluslararası Kredi Notu Düştü",
        "get_description": lambda: (
            "Kredi Derecelendirme Kuruluşlarından Kötü Haber!",
            "Artan jeopolitik riskler ve ülkenin borçlanma seviyesi nedeniyle, uluslararası bir kredi "
            "derecelendirme kuruluşu ülkenin notunu düşürdü. Bu karar, hem hazineyi ek bir yük altına soktu "
            "hem de bürokraside bir moral bozukluğuna yol açtı."
        ),
        "effects": {
            "treasury": -30000,
            "bureaucratic_efficiency": -5
        },
        "type": "negative"
    },
    {
        "name": "Başarılı Diplomatik Ziyaret",
        "get_description": lambda: (
            "Uluslararası Arenada Önemli Kazanım!",
            "Liderliğinizde gerçekleştirilen başarılı bir diplomatik ziyaret, komşu ülkelerle "
            "yeni bir ticaret anlaşmasının kapısını araladı. Bu gelişme, lider olarak konumunuzu "
            "güçlendirirken, kamuoyunda da büyük bir memnuniyetle karşılandı."
        ),
        "effects": {
            "political_capital": +10,
            "public_support": +5
        },
        "type": "positive"
    }
]

def get_random_event():
    """Havuzdan rastgele bir olay seçer ve döndürür."""
    return random.choice(EVENTS)
