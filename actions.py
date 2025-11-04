# -*- coding: utf-8 -*-

"""
actions.py: Oyuncunun seçebileceği tüm eylemleri ve etkilerini içerir.
Her eylem, bir maliyeti ve çeşitli oyun kaynakları üzerindeki etkileri
olan bir sözlük olarak tanımlanmıştır.
"""

ACTIONS = {
    "1": {
        "name": "Geniş Kapsamlı Miting Düzenle",
        "description": "Halkın desteğini artırmak için büyük bir miting düzenle. Yüksek maliyetlidir.",
        "effects": {
            "political_capital": -10,
            "public_support": +15,
            "treasury": -40000,
            "factions": {
                # Parti özelinde etki gösterecek, genel bir etki şablonu
                "Şahinler": +5,
                "Popülistler": +10, # Örnek fraksiyon
                "Gelenekçiler": -5
            }
        }
    },
    "2": {
        "name": "Propaganda Kampanyası Başlat",
        "description": "Partinin ideolojik duruşunu güçlendir ve parti içi tutarlılığı artır.",
        "effects": {
            "cohesion": +15,
            "public_support": +5,
            "treasury": -25000,
            "factions": {
                "Parti Ortodoksları": +10,
                "Yenilikçiler": -5, # Örnek
                "Merkezciler": -5
            }
        }
    },
    "3": {
        "name": "Bürokratik Reformu Hızlandır",
        "description": "Kararların daha hızlı uygulanması için bürokrasiyi iyileştir. Liderlik otoritesini zorlar.",
        "effects": {
            "bureaucratic_efficiency": +10,
            "political_capital": -15,
            "cohesion": -5,
            "treasury": -50000,
            "factions": {
                "Teknokratlar": +15,
                "Bürokratlar": +10,
                "Gelenekçiler": -10
            }
        }
    },
    "4": {
        "name": "Yerel Teşkilatları Ziyaret Et",
        "description": "Parti içi gerilimi azaltmak ve siyasi otoriteyi pekiştirmek için yerel liderlerle görüş.",
        "effects": {
            "political_capital": +10,
            "cohesion": +5,
            "treasury": -10000,
            "factions": {
                "Yerel Temsilciler": +15,
                "Merkezciler": +5,
                "Şahinler": -5
            }
        }
    },
    "5": {
        "name": "Büyük Şirketlerden Bağış Topla",
        "description": "Parti hazinesini doldurmak için özel sektörden fon sağla. Yolsuzluk algısını artırır.",
        "effects": {
            "treasury": +100000,
            "political_capital": -5,
            "public_support": -5,
            "risky_action": 1, # Yolsuzluk Algısını artırır
            "factions": {
                "Serbest Piyasacılar": +10,
                "Sendikacılar": -15
            }
        }
    },
    "6": {
        "name": "Popülist Sosyal Yardım Vaadi",
        "description": "Kamuoyu desteğini anında artıracak bir sosyal yardım paketi vaat et. Pahalıdır.",
        "effects": {
            "public_support": +20,
            "political_capital": -5,
            "cohesion": -10,
            "treasury": -75000,
            "factions": {
                "Sosyal Destekçiler": +15,
                "Ekonomik Realistler": -10
            }
        }
    },
    "7": {
        "name": "Parti İçi Disiplini Sağla",
        "description": "Parti içi ideolojik tutarlılığı sağlamak için otoriteni kullan. Bazı fraksiyonları küstürebilir.",
        "effects": {
            "cohesion": +20,
            "political_capital": -10,
            "public_support": -5,
            "factions": {
                "Parti Ortodoksları": +15,
                "Bireysel Hakçılar": -10,
                "Yenilikçiler": -10
            }
        }
    }
}
