# -*- coding: utf-8 -*-

"""
parties.py: Oyunun tüm statik başlangıç verilerini içerir.
Bu dosya, partilerin, bölgelerin, ideolojilerin ve oyun dünyasının
değişmeyen tüm niteliklerini merkezi bir yerde toplar.
"""

PARTIES = {
    "Ulusal Birlik Partisi": {
        "emoji": "🐺",
        "ideology": "Sıkı Milliyetçilik",
        "slogan": "Tek Vatan, Tek Yürek!",
        "description": "Devletin bölünmez bütünlüğünü ve ulusal egemenliği her şeyin üzerinde tutan, köklü bir parti. Güçlü bir ordu ve merkeziyetçi bir yönetim anlayışını savunur.",
        "initial_resources": {
            "political_capital": 65, "cohesion": 70,
            "bureaucratic_efficiency": 45, "public_support": 40,
            "treasury": 70000
        },
        "factions": {
            "Şahinler": {"satisfaction": 70, "description": "Askeri çözümleri ve sert gücü savunan kanat."},
            "Merkezciler": {"satisfaction": 65, "description": "Partinin geleneksel çizgisini korumaya odaklı, dengeli kanat."},
            "Anadolucular": {"satisfaction": 75, "description": "Kültürel ve geleneksel değerlerin korunmasını önceliklendiren kanat."}
        }
    },
    "Özgürlük ve Demokrasi Hareketi": {
        "emoji": "🗽",
        "ideology": "Liberalizm",
        "slogan": "Birey Özgür, Toplum Güçlü!",
        "description": "Bireysel hak ve özgürlükleri, serbest piyasa ekonomisini ve sivil toplumu merkeze alan bir hareket. Ekonomik kalkınma ve inovasyona büyük önem verir.",
        "initial_resources": {
            "political_capital": 55, "cohesion": 50,
            "bureaucratic_efficiency": 75, "public_support": 35,
            "treasury": 150000
        },
        "factions": {
            "Serbest Piyasacılar": {"satisfaction": 72, "description": "Vergi indirimleri ve tam rekabeti savunan ekonomik kanat."},
            "Sosyal Liberaller": {"satisfaction": 68, "description": "Eğitim ve sağlıkta fırsat eşitliğini savunan vicdani kanat."},
            "Teknokratlar": {"satisfaction": 75, "description": "Devlet yönetiminde veriye ve liyakate dayalı politikaları destekleyen kanat."}
        }
    },
    "Adalet ve Refah Partisi": {
        "emoji": "🕌",
        "ideology": "Muhafazakâr Demokrasi",
        "slogan": "Halka Hizmet, Hakka Hizmettir!",
        "description": "Toplumun geleneksel ve manevi değerlerini koruyarak, sosyal adalet ve refahı artırmayı hedefleyen geniş tabanlı bir parti.",
        "initial_resources": {
            "political_capital": 70, "cohesion": 75,
            "bureaucratic_efficiency": 55, "public_support": 45,
            "treasury": 110000
        },
        "factions": {
            "Gelenekçiler": {"satisfaction": 75, "description": "Partinin kuruluş felsefesine ve manevi değerlere sıkı sıkıya bağlı kanat."},
            "Yenilikçiler": {"satisfaction": 65, "description": "Küresel gelişmelere ve yeni nesle hitap eden reformları destekleyen kanat."},
            "Sosyal Yardım Gönüllüleri": {"satisfaction": 70, "description": "Yerel yönetimler ve sivil toplum aracılığıyla sosyal yardımları organize eden kanat."}
        }
    },
    "Halkın Gücü Partisi": {
        "emoji": "✊",
        "ideology": "Demokratik Sosyalizm",
        "slogan": "Eşitlik, Adalet, Emek!",
        "description": "Emekçinin ve ezilenin hakkını savunan, kamucu politikaları ve sendikal örgütlenmeyi temel alan bir parti.",
        "initial_resources": {
            "political_capital": 45, "cohesion": 80,
            "bureaucratic_efficiency": 35, "public_support": 30,
            "treasury": 40000
        },
        "factions": {
            "Sendikacılar": {"satisfaction": 75, "description": "İşçi hakları ve sendikal mücadeleyi önceliklendiren, partinin bel kemiği."},
            "Akademisyenler": {"satisfaction": 60, "description": "Partinin ideolojik çizgisini ve politikalarını teorik düzeyde geliştiren entelektüel kanat."},
            "Gençlik Kolları": {"satisfaction": 78, "description": "Sokakta aktif, enerjik ve radikal eylemleri savunan dinamik grup."}
        }
    },
    "Çevre ve Yeşil Yaşam Partisi": {
        "emoji": "🌳",
        "ideology": "Ekolojizm",
        "slogan": "Gelecek Yeşil Olacak!",
        "description": "Doğal yaşamın korunmasını ve sürdürülebilir kalkınmayı savunan, çevre politikalarını merkeze alan bir parti.",
        "initial_resources": {"political_capital": 40, "cohesion": 60, "bureaucratic_efficiency": 65, "public_support": 25, "treasury": 50000},
        "factions": {
            "Radikal Aktivistler": {"satisfaction": 62, "description": "Sivil itaatsizlik ve doğrudan eylemi savunan, uzlaşmaz kanat."},
            "Pragmatik Yeşiller": {"satisfaction": 75, "description": "Çevre politikalarını ekonomiyle dengelemeyi amaçlayan, reformcu kanat."}
        }
    },
    "Reform ve Teknoloji Partisi": {
        "emoji": "🔬",
        "ideology": "Teknokrasi",
        "slogan": "Akılla Yönet, Geleceği Fethet!",
        "description": "Bilim, teknoloji ve veriye dayalı yönetimi savunan; liyakat ve verimliliği temel alan bir parti.",
        "initial_resources": {"political_capital": 50, "cohesion": 55, "bureaucratic_efficiency": 85, "public_support": 20, "treasury": 130000},
        "factions": {
            "İlericiler": {"satisfaction": 70, "description": "Teknolojik gelişimi ve sosyal reformları hızlandırmak isteyen kanat."},
            "Bürokratlar": {"satisfaction": 75, "description": "Devletin mevcut yapısını verimlilik esasıyla yeniden düzenlemeyi amaçlayan kanat."}
        }
    },
    "Bölgesel Otonomi Cephesi": {
        "emoji": "🌍",
        "ideology": "Federalizm",
        "slogan": "Yerinden Yönetim, Gerçek Demokrasi!",
        "description": "Merkezi yönetimin yetkilerinin yerel yönetimlere devredilmesini savunan, kültürel çeşitliliğe önem veren bir cephe.",
        "initial_resources": {"political_capital": 35, "cohesion": 85, "public_support": 40, "treasury": 60000},
        "factions": {
            "Yerel Temsilciler": {"satisfaction": 78, "description": "Bölgelerin kendi meclisleri tarafından yönetilmesini savunan çekirdek grup."},
            "Merkez Karşıtları": {"satisfaction": 72, "description": "Merkezi hükümetin her türlü müdahalesine ideolojik olarak karşı çıkan kanat."}
        }
    },
    "Tarafsızlar Birliği": {
        "emoji": "⚖️",
        "ideology": "Pragmatizm",
        "slogan": "Ne Sağ, Ne Sol, Tek Yol Akıl!",
        "description": "İdeolojik kamplaşmalara karşı, sorunlara akılcı ve duruma özel çözümler bulmayı amaçlayan bir oluşum.",
        "initial_resources": {"political_capital": 60, "cohesion": 40, "bureaucratic_efficiency": 70, "public_support": 15, "treasury": 90000},
        "factions": {
            "Anti-Politika": {"satisfaction": 60, "description": "Mevcut siyasi partilerin tamamını yozlaşmış olarak gören grup."},
            "Ekonomik Realistler": {"satisfaction": 70, "description": "İdeoloji yerine ekonomik verilere dayalı kararlar alınmasını savunan kanat."}
        }
    }
}

REGIONS = {
    "Marmara (İstanbul)": {"sensitivities": {"immigrant": 50, "inequality": 80, "polarization": 70}},
    "İç Anadolu (Ankara)": {"sensitivities": {"immigrant": 40, "inequality": 60, "polarization": 80}},
    "Ege (İzmir)": {"sensitivities": {"immigrant": 20, "inequality": 50, "polarization": 60}},
    "Akdeniz (Antalya)": {"sensitivities": {"immigrant": 30, "inequality": 40, "polarization": 50}},
    "Karadeniz (Trabzon)": {"sensitivities": {"immigrant": 70, "inequality": 30, "polarization": 40}},
    "Güneydoğu Anadolu (Diyarbakır)": {"sensitivities": {"immigrant": 60, "inequality": 90, "polarization": 90}},
    "Doğu Anadolu (Erzurum)": {"sensitivities": {"immigrant": 80, "inequality": 70, "polarization": 50}},
    "Sanayi Bölgesi (Kocaeli)": {"sensitivities": {"immigrant": 60, "inequality": 85, "polarization": 65}},
    "Tarım Merkezi (Konya)": {"sensitivities": {"immigrant": 50, "inequality": 40, "polarization": 30}},
    "Kültürel Başkent (Eskişehir)": {"sensitivities": {"immigrant": 10, "inequality": 65, "polarization": 75}}
}

# Her bölgeye partilerin doğal çekimini (başlangıç oy potansiyeli) ata
# Bu değerler partinin ideolojisi ve bölgenin yapısına göre belirlenmiştir
_attraction_data = {
    "Marmara (İstanbul)":               {"UBP": 15, "ÖDH": 25, "ARP": 20, "HGP": 15, "ÇYYP": 10, "RTP": 15, "BÖC": 5, "TB": 5},
    "İç Anadolu (Ankara)":              {"UBP": 25, "ÖDH": 15, "ARP": 30, "HGP": 5, "ÇYYP": 5, "RTP": 10, "BÖC": 0, "TB": 10},
    "Ege (İzmir)":                      {"UBP": 10, "ÖDH": 35, "ARP": 15, "HGP": 15, "ÇYYP": 15, "RTP": 5, "BÖC": 5, "TB": 5},
    "Akdeniz (Antalya)":                {"UBP": 20, "ÖDH": 30, "ARP": 25, "HGP": 5, "ÇYYP": 10, "RTP": 5, "BÖC": 5, "TB": 5},
    "Karadeniz (Trabzon)":              {"UBP": 35, "ÖDH": 5, "ARP": 40, "HGP": 5, "ÇYYP": 5, "RTP": 0, "BÖC": 0, "TB": 10},
    "Güneydoğu Anadolu (Diyarbakır)":   {"UBP": 10, "ÖDH": 10, "ARP": 10, "HGP": 25, "ÇYYP": 5, "RTP": 0, "BÖC": 35, "TB": 5},
    "Doğu Anadolu (Erzurum)":           {"UBP": 40, "ÖDH": 5, "ARP": 35, "HGP": 5, "ÇYYP": 0, "RTP": 0, "BÖC": 10, "TB": 5},
    "Sanayi Bölgesi (Kocaeli)":         {"UBP": 20, "ÖDH": 20, "ARP": 25, "HGP": 20, "ÇYYP": 5, "RTP": 5, "BÖC": 0, "TB": 5},
    "Tarım Merkezi (Konya)":             {"UBP": 25, "ÖDH": 10, "ARP": 45, "HGP": 5, "ÇYYP": 5, "RTP": 0, "BÖC": 0, "TB": 10},
    "Kültürel Başkent (Eskişehir)":     {"UBP": 10, "ÖDH": 30, "ARP": 10, "HGP": 20, "ÇYYP": 15, "RTP": 10, "BÖC": 0, "TB": 5}
}
_party_keys = {
    "UBP": "Ulusal Birlik Partisi", "ÖDH": "Özgürlük ve Demokrasi Hareketi",
    "ARP": "Adalet ve Refah Partisi", "HGP": "Halkın Gücü Partisi",
    "ÇYYP": "Çevre ve Yeşil Yaşam Partisi", "RTP": "Reform ve Teknoloji Partisi",
    "BÖC": "Bölgesel Otonomi Cephesi", "TB": "Tarafsızlar Birliği"
}
for region_name, attractions in _attraction_data.items():
    REGIONS[region_name]["natural_attraction"] = {
        _party_keys[short]: value for short, value in attractions.items()
    }
