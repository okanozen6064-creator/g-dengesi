# -*- coding: utf-8 -*-
"""
actions.py: Oyuncunun seçebileceği tüm eylemleri ve etkilerini içerir.
Part 3: Eylemler "Politika" ve "Propaganda" olarak ikiye ayrılmış ve
içerik manifestoya uygun olarak 10'ar adetle zenginleştirilmiştir.
"""

POLITIKA_ACTIONS = {
    "POL_VERGI_REFORMU": {
        "name": "📜 Kapsamlı Vergi Reformu",
        "description": "Ekonomiyi canlandırmak için vergi oranlarını yeniden düzenle. Zengin ve fakir kesim arasında gerilime yol açabilir.",
        "ep_cost": 2,
        "effects": {"treasury": 75000, "public_support": -10, "cohesion": -15, "political_capital": -10}
    },
    "POL_TABLET_DAGITIMI": {
        "name": "📜 Eğitimde Fırsat Eşitliği",
        "description": "Öğrencilere ücretsiz tablet dağıtarak teknoloji okuryazarlığını artır. Popülist bir hamle olarak görülebilir.",
        "ep_cost": 1,
        "effects": {"treasury": -60000, "public_support": +15, "bureaucratic_efficiency": -5}
    },
    "POL_SINIR_GUVENLIGI": {
        "name": "📜 Sınır Güvenliğini Artır",
        "description": "Sınırlara duvar örülmesi ve teknolojik denetimlerin artırılması. Milliyetçi kanadı memnun eder.",
        "ep_cost": 2,
        "effects": {"treasury": -100000, "cohesion": +10, "public_support": +5, "political_capital": -5}
    },
    "POL_KOPRU_PROJESI": {
        "name": "📜 Asrın Köprü Projesi",
        "description": "İki yakayı birleştirecek dev bir altyapı projesi başlat. Yüksek maliyetlidir ve yolsuzluk riski taşır.",
        "ep_cost": 2,
        "effects": {"treasury": -150000, "public_support": +20, "risky_action": 1}
    },
    "POL_KARBON_VERGISI": {
        "name": "📜 Karbon Vergisi Yasası",
        "description": "Çevre kirliliğini azaltmak için sanayi tesislerine yeni vergiler getir. Yeşil seçmeni etkiler, sanayicileri kızdırır.",
        "ep_cost": 1,
        "effects": {"treasury": 40000, "public_support": +5, "cohesion": -10}
    },
    "POL_BUROKRATIK_REFORM": {
        "name": "📜 Bürokratik Reformu Hızlandır",
        "description": "Kararların daha hızlı uygulanması için bürokrasiyi iyileştir. Liderlik otoritesini zorlar.",
        "ep_cost": 2,
        "effects": {"bureaucratic_efficiency": +10, "political_capital": -15, "cohesion": -5, "treasury": -50000}
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
    "POL_TARIM_DESTEGI": {
        "name": "📜 Tarım Destek Paketini Açıkla",
        "description": "Çiftçilere yönelik sübvansiyonları artırarak kırsal kesimin oyunu kazan. Şehirli seçmen tepki gösterebilir.",
        "ep_cost": 1,
        "effects": {"treasury": -70000, "public_support": +10, "cohesion": +5}
    },
    "POL_TEKNOLOJI_YATIRIMI": {
        "name": "📜 Ulusal Teknoloji Hamlesi",
        "description": "Yerli teknoloji şirketlerine ve AR-GE'ye büyük bir fon ayır. Uzun vadede bürokrasiyi iyileştirir.",
        "ep_cost": 2,
        "effects": {"treasury": -90000, "bureaucratic_efficiency": +15, "political_capital": -5}
    }
}

PROPAGANDA_ACTIONS = {
    "PROP_MITING": {
        "name": "📢 Geniş Kapsamlı Miting",
        "description": "Halkın desteğini artırmak için büyük bir miting düzenle. Yüksek maliyetlidir.",
        "ep_cost": 2,
        "effects": {"political_capital": -10, "public_support": +15, "treasury": -40000}
    },
    "PROP_KAMPANYA": {
        "name": "📢 İdeolojik Propaganda Kampanyası",
        "description": "Partinin ideolojik duruşunu güçlendir ve parti içi tutarlılığı artır.",
        "ep_cost": 1,
        "effects": {"cohesion": +15, "public_support": +5, "treasury": -25000}
    },
    "PROP_RAKIP_LIDER": {
        "name": "📢 Rakip Liderin Geçmişini Araştır",
        "description": "Rakip liderin eski ve çelişkili röportajlarını bulup medyaya sızdır. Kirli bir oyundur.",
        "ep_cost": 1,
        "effects": {"public_support": +10, "political_capital": -10, "risky_action": 1}
    },
    "PROP_SOSYAL_MEDYA": {
        "name": "📢 Sosyal Medya Algoritması Manipülasyonu",
        "description": "Genç seçmen kitlesine yönelik mikro hedefleme yap. Yüksek KOD artışı, yüksek Yolsuzluk Algısı riski.",
        "ep_cost": 1,
        "effects": {"treasury": -50000, "public_support": +15, "risky_action": 2}
    },
    "PROP_BELGESEL": {
        "name": "📢 Parti Tarihi Belgeseli Finanse Et",
        "description": "Partinin köklü geçmişini ve başarılarını anlatan bir belgesel hazırla. Uzun vadeli bir yatırımdır.",
        "ep_cost": 2,
        "effects": {"treasury": -80000, "cohesion": +20, "public_support": +5}
    },
    "PROP_GAZETE": {
        "name": "📢 Gazete Manşetlerini Etkile",
        "description": "Yakın olduğun bir medya grubunun manşetlerini kendi lehine çevir. Medya etiğini zedeler.",
        "ep_cost": 1,
        "effects": {"treasury": -30000, "public_support": +10, "political_capital": -5}
    },
    "PROP_UNLU_DESTEGI": {
        "name": "📢 Ünlü İsimlerden Destek Al",
        "description": "Popüler bir sanatçı veya sporcunun partine açık destek vermesini sağla. Geri tepebilir.",
        "ep_cost": 1,
        "effects": {"treasury": -40000, "public_support": +12}
    },
    "PROP_KAPI_KAPI": {
        "name": "📢 Kapı Kapı Dolaşma Kampanyası",
        "description": "Parti gönüllülerini organize ederek seçmenlerle birebir temas kur. Yavaş ama etkilidir.",
        "ep_cost": 2,
        "effects": {"cohesion": +5, "public_support": +10}
    },
    "PROP_VAAT_KILAVUZU": {
        "name": "📢 'Gelecek Vizyonu' Vaat Kılavuzu",
        "description": "Partinin gelecek 10 yıl için vaatlerini içeren parlak ve süslü bir kitapçık bastırıp dağıt.",
        "ep_cost": 1,
        "effects": {"treasury": -35000, "public_support": +8, "bureaucratic_efficiency": -5}
    },
    "PROP_ANKET_MANIPULASYONU": {
        "name": "📢 Anket Sonuçlarını Sızdır",
        "description": "Partinizi önde gösteren bir anket sonucunu 'yanlışlıkla' basına sızdır. Güvenilirlik riski taşır.",
        "ep_cost": 1,
        "effects": {"public_support": +7, "political_capital": -5, "risky_action": 1}
    }
}
