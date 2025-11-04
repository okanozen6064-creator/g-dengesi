# -*- coding: utf-8 -*-
"""
actions.py: Oyuncunun seçebileceği tüm eylemleri ve etkilerini içerir.
Part 4: Eylemler "İktidar", "Muhalefet" ve "Genel" olarak ayrılmış,
ittifak mekaniği eklenmiştir.
"""

# Tüm partilerin her durumda kullanabileceği genel eylemler
GENEL_ACTIONS = {
    "PROP_MITING": {
        "name": "📢 Geniş Kapsamlı Miting",
        "description": "Halkın desteğini artırmak için büyük bir miting düzenle. Yüksek maliyetlidir.",
        "ep_cost": 2,
        "effects": {"political_capital": -10, "public_support": +15, "treasury": -40000}
    },
    "PROP_SOSYAL_MEDYA": {
        "name": "📢 Sosyal Medya Algoritması Manipülasyonu",
        "description": "Genç seçmen kitlesine yönelik mikro hedefleme yap. Yüksek KOD artışı, yüksek Yolsuzluk Algısı riski.",
        "ep_cost": 1,
        "effects": {"treasury": -50000, "public_support": +15, "risky_action": 2}
    },
    "POL_BAGIS_TOPLA": {
        "name": "📜 Büyük Şirketlerden Bağış Topla",
        "description": "Parti hazinesini doldurmak için özel sektörden fon sağla. Yolsuzluk algısını artırır.",
        "ep_cost": 1,
        "effects": {"treasury": 80000, "political_capital": -5, "public_support": -5, "risky_action": 1}
    },
    "POL_DISIPLIN_SAGLA": {
        "name": "📜 Parti İçi Disiplini Sağla",
        "description": "Parti içi ideolojik tutarlılığı sağlamak için otoriteni kullan. Bazı fraksiyonları küstürebilir.",
        "ep_cost": 1,
        "effects": {"cohesion": +20, "political_capital": -10, "public_support": -5}
    },
}

# Sadece "Muhalefet" durumundayken kullanılabilecek eylemler
MUHALEFET_ACTIONS = {
    "MUH_SORUSTURMA": {
        "name": "🔎 Soruşturma Çağrısı",
        "description": "İktidar partisinin yolsuzluk yaptığını iddia ederek mecliste soruşturma açılmasını talep et. Geri tepebilir.",
        "ep_cost": 1,
        "effects": {"political_capital": +10, "public_support": -5} # Başarı/başarısızlık olasılığı eklenecek
    },
    "MUH_PROTESTO": {
        "name": "🗣️ Halk Protestosu Örgütle",
        "description": "İktidarın bir politikasına karşı halkı sokağa davet et. Kontrolden çıkma riski var.",
        "ep_cost": 2,
        "effects": {"public_support": +15, "cohesion": -10, "risky_action": 1}
    },
    "MUH_GOLGE_KABINE": {
        "name": "👥 Gölge Kabine Kur",
        "description": "Partinin uzman isimlerinden oluşan bir gölge kabine ile iktidarın her adımını takip et. Ciddiyetini artırır.",
        "ep_cost": 1,
        "effects": {"bureaucratic_efficiency": +10, "political_capital": +5}
    },
     "MUH_ITTİFAK_GORUSMESI": {
        "name": "🤝 İttifak Görüşmesi Başlat",
        "description": "Meclis'te çoğunluğu sağlamak için başka bir partiyle ittifak kurmayı dene. İdeolojik uyum ve siyasi güç gerektirir.",
        "ep_cost": 2,
        "effects": {} # Bu eylemin etkisi özel olarak `game_state` içinde ele alınacak
    },
}

# Sadece "İktidar" durumundayken kullanılabilecek eylemler
IKTIDAR_ACTIONS = {
    "IKT_BUROKRASI": {
        "name": " streamline ️ Bürokratik Basitleştirme",
        "description": "Devlet işleyişini hızlandırmak için gereksiz prosedürleri kaldır. Bürokratların tepkisini çekebilir.",
        "ep_cost": 1,
        "effects": {"bureaucratic_efficiency": +15, "cohesion": -5}
    },
    "IKT_KEMER_SIKMA": {
        "name": "💰 Kemer Sıkma Politikası",
        "description": "Devlet harcamalarını kısarak Hazine'yi güçlendir. Halkın tepkisine yol açar.",
        "ep_cost": 2,
        "effects": {"treasury": +100000, "public_support": -20}
    },
    "IKT_POPULIST_MUJDE": {
        "name": "🎉 Popülist Müjde Açıkla",
        "description": "Yaklaşan seçimler öncesi halka yönelik bir 'müjde' paketi açıkla. Bütçeyi sarsar ama oy oranını fırlatır.",
        "ep_cost": 1,
        "effects": {"public_support": +25, "treasury": -80000}
    }
}
