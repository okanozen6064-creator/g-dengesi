# -*- coding: utf-8 -*-
"""
events.py: Oyun içinde tetiklenebilecek rastgele olayları ve interaktif önergeleri içerir.
Part 3: İçerik, 10+ adet interaktif önerge ile zenginleştirilmiştir.
"""

import random

# Yıl başında otomatik tetiklenen basit olaylar
EVENTS = [
    {"name": "Ekonomik Canlanma", "description": "Uluslararası piyasalardaki olumlu hava sayesinde Hazine'ye ek gelir aktarıldı.", "effects": {"treasury": 50000, "public_support": 5}},
    {"name": "Yolsuzluk Sızıntısı", "description": "Partinizin üst düzey bir yöneticisinin adı bir skandala karıştı. Güven kaybı yaşandı.", "effects": {"political_capital": -15, "public_support": -10, "cohesion": -5}},
    {"name": "Kredi Notu Düştü", "description": "Uluslararası kredi derecelendirme kuruluşları ülkenin notunu düşürdü. Hazine ek yük altına girdi.", "effects": {"treasury": -30000, "bureaucratic_efficiency": -5}},
    {"name": "Başarılı Diplomatik Ziyaret", "description": "Komşu ülkelerle yeni bir ticaret anlaşmasının kapısı aralandı. Liderliğiniz güçlendi.", "effects": {"political_capital": +10, "public_support": +5}}
]

# "Karar Al" butonuyla tetiklenen, oyuncuya seçenek sunan interaktif önergeler
PROPOSALS = [
    {
        "name": "Yerel Yönetimlere Otonomi Yasası",
        "description": "Bir bölgesel partiden gelen bu yasa, merkezi otoriteyi zayıflatma potansiyeli taşıyor. Kabulü, partinin Milliyetçi kanadını öfkelendirecektir.",
        "choices": {
            "Kabul Et": {"political_capital": -15, "cohesion": -10, "public_support": +5},
            "Reddet": {"political_capital": +10, "cohesion": +5, "public_support": -5}
        }
    },
    {
        "name": "Finansal Şeffaflık Yasası",
        "description": "Yolsuzluk algısını düşürmek için ideal, ancak parti finansmanını zora sokacak şeffaflık kuralları getiriyor.",
        "choices": {
            "Destekle": {"risky_action": -2, "treasury": -40000, "public_support": +10},
            "Karşı Çık": {"risky_action": 1, "treasury": +20000, "public_support": -10}
        }
    },
    {
        "name": "Ulusal Tatil Günlerinin Artırılması",
        "description": "Halkın mutluluğunu artırır, ancak sanayi ve ekonomi şahinlerinin sert tepkisine yol açar.",
        "choices": {
            "Onayla": {"public_support": +15, "treasury": -25000, "cohesion": -5},
            "Veto Et": {"public_support": -10, "treasury": +10000, "cohesion": +5}
        }
    },
    {
        "name": "Sansür Yasası Teklifi",
        "description": "Muhalif basını susturmaya yönelik bu teklif, partinin otoriter kanadını memnun edecek ancak özgürlükçüleri kızdıracaktır.",
        "choices": {
            "Meclise Getir": {"political_capital": +15, "public_support": -15, "cohesion": +10},
            "Gündemden Düşür": {"political_capital": -10, "public_support": +10, "cohesion": -10}
        }
    },
    {
        "name": "Zorunlu Askerlik Süresinin Kısaltılması",
        "description": "Genç seçmenler arasında popüler olacak bir hamle, ancak ordunun ve milliyetçi kesimin tepkisini çekecektir.",
        "choices": {
            "Yasalaştır": {"public_support": +12, "political_capital": -10, "cohesion": -8},
            "Teklifi Reddet": {"public_support": -8, "political_capital": +5, "cohesion": +10}
        }
    },
    {
        "name": "Nükleer Santral İnşaatı",
        "description": "Enerji bağımsızlığı için kritik bir adım, fakat çevre örgütleri ve yerel halk büyük bir protesto hazırlığında.",
        "choices": {
            "Projeyi Başlat": {"bureaucratic_efficiency": +10, "treasury": -200000, "public_support": -5},
            "Projeyi İptal Et": {"bureaucratic_efficiency": -5, "public_support": +10}
        }
    },
    {
        "name": "Sendikal Hakların Genişletilmesi",
        "description": "İşçi sınıfının desteğini kazanmak için harika bir fırsat, ancak büyük şirketler ve yatırımcılar bu durumdan hoşlanmayacak.",
        "choices": {
            "Grev Hakkını Genişlet": {"public_support": +10, "treasury": -30000, "cohesion": +5},
            "Mevcut Durumu Koru": {"public_support": -5, "treasury": +15000, "cohesion": -5}
        }
    },
    {
        "name": "İnanç Özgürlüğü Yasası",
        "description": "Azınlık gruplarının takdirini kazanacak bu yasa, partinin muhafazakar tabanında rahatsızlık yaratabilir.",
        "choices": {
            "Özgürlükleri Genişlet": {"cohesion": -15, "public_support": +8, "political_capital": -5},
            "Statükoyu Koru": {"cohesion": +10, "public_support": -5}
        }
    },
    {
        "name": "İnternet Servis Sağlayıcılarına Vergi",
        "description": "Teknoloji devlerinden alınacak yeni bir vergi Hazine'yi doldurabilir, ancak internet faturalarını artırarak halkı kızdırabilir.",
        "choices": {
            "Vergiyi Getir": {"treasury": +60000, "public_support": -12},
            "Vazgeç": {"treasury": -10000, "public_support": +5}
        }
    },
    {
        "name": "Kültürel Mirasın Korunması Fonu",
        "description": "Tarihi eserlerin restorasyonu için büyük bir fon ayrılması entelektüel kesimi memnun eder, ancak popülist bir hamle değildir.",
        "choices": {
            "Fonu Onayla": {"treasury": -50000, "cohesion": +5, "public_support": +3},
            "Bütçeyi Başka Yere Aktar": {"treasury": +20000, "public_support": -3}
        }
    }
]

def get_random_event():
    """Havuzdan rastgele bir yıl başı olayı seçer."""
    if random.random() < 0.7: # Her yıl %70 ihtimalle olay olsun
        return random.choice(EVENTS)
    return None

def get_random_proposal():
    """Havuzdan rastgele bir interaktif önerge seçer."""
    return random.choice(PROPOSALS)
