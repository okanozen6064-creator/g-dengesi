# -*- coding: utf-8 -*-

"""
actions.py: Oyuncunun seçebileceği tüm eylemleri ve etkilerini içerir.
Her eylem, bir maliyeti (EP, Hazine, Kaynaklar) ve çeşitli oyun
kaynakları üzerindeki etkileri olan bir sözlük olarak tanımlanmıştır.
"""

ACTIONS = {
    "1": {
        "name": "Geniş Kapsamlı Miting Düzenle",
        "description": "Halkın desteğini artırmak için büyük bir miting düzenle. Yüksek maliyetlidir ve tüm enerjini alır.",
        "ep_cost": 2,
        "effects": {
            "political_capital": -10, "public_support": +15, "treasury": -40000,
            "factions": {"Şahinler": +5, "Merkezciler": -5}
        }
    },
    "2": {
        "name": "Propaganda Kampanyası Başlat",
        "description": "Partinin ideolojik duruşunu güçlendir ve parti içi tutarlılığı artır.",
        "ep_cost": 1,
        "effects": {
            "cohesion": +15, "public_support": +5, "treasury": -25000,
            "factions": {"Anadolucular": +10, "Sosyal Liberaller": -5}
        }
    },
    "3": {
        "name": "Bürokratik Reformu Hızlandır",
        "description": "Kararların daha hızlı uygulanması için bürokrasiyi iyileştir. Liderlik otoritesini zorlar.",
        "ep_cost": 2,
        "effects": {
            "bureaucratic_efficiency": +10, "political_capital": -15, "cohesion": -5, "treasury": -50000,
            "factions": {"Teknokratlar": +15, "Gelenekçiler": -10}
        }
    },
    "4": {
        "name": "Yerel Teşkilatları Ziyaret Et",
        "description": "Parti içi gerilimi azaltmak ve siyasi otoriteyi pekiştirmek için yerel liderlerle görüş.",
        "ep_cost": 1,
        "effects": {
            "political_capital": +10, "cohesion": +5, "treasury": -10000,
            "factions": {"Merkezciler": +10, "Şahinler": -5}
        }
    },
    "5": {
        "name": "Büyük Şirketlerden Bağış Topla",
        "description": "Parti hazinesini doldurmak için özel sektörden fon sağla. Yolsuzluk algısını artırır.",
        "ep_cost": 1,
        "effects": {
            "treasury": +80000, "political_capital": -5, "public_support": -5, "risky_action": 1,
            "factions": {"Serbest Piyasacılar": +10, "Sendikacılar": -15}
        }
    },
    "6": {
        "name": "Popülist Sosyal Yardım Vaadi",
        "description": "Kamuoyu desteğini anında artıracak bir sosyal yardım paketi vaat et. Pahalıdır ve partiyi bölebilir.",
        "ep_cost": 1,
        "effects": {
            "public_support": +20, "political_capital": -5, "cohesion": -10, "treasury": -60000,
            "factions": {"Sosyal Yardım Gönüllüleri": +15, "Ekonomik Realistler": -10}
        }
    },
    "7": {
        "name": "Parti İçi Disiplini Sağla",
        "description": "Parti içi ideolojik tutarlılığı sağlamak için otoriteni kullan. Bazı fraksiyonları küstürebilir.",
        "ep_cost": 1,
        "effects": {
            "cohesion": +20, "political_capital": -10, "public_support": -5,
            "factions": {"Gelenekçiler": +10, "Sosyal Liberaller": -10}
        }
    }
}
