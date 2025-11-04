# -*- coding: utf-8 -*-

"""
config.py: Oyunun tüm statik başlangıç verilerini içerir.
Bu dosya, partilerin, bölgelerin ve diğer değişmeyen oyun içi varlıkların
başlangıçtaki tüm niteliklerini merkezi bir yerde toplar.
"""

# 8 Siyasi Partinin Başlangıç Değerleri ve Fraksiyonları
# Kaynaklar 0-100 ölçeğinde, Hazine ise mutlak bir değerdir.
# Fraksiyon memnuniyetleri %60-75 aralığında başlar.
PARTIES = {
    "Ulusal Birlik Partisi": {
        "ideology": "Sıkı Milliyetçilik",
        "initial_resources": {
            "political_capital": 75,
            "cohesion": 65,
            "bureaucratic_efficiency": 40,
            "public_support": 60,
            "treasury": 100000
        },
        "factions": {
            "Şahinler": {"satisfaction": 70},
            "Merkezciler": {"satisfaction": 65},
            "İhtiyatlılar": {"satisfaction": 75}
        }
    },
    "Özgürlük ve Demokrasi Hareketi": {
        "ideology": "Liberalizm",
        "initial_resources": {
            "political_capital": 60,
            "cohesion": 55,
            "bureaucratic_efficiency": 70,
            "public_support": 50,
            "treasury": 200000
        },
        "factions": {
            "Serbest Piyasacılar": {"satisfaction": 72},
            "Bireysel Hakçılar": {"satisfaction": 68},
            "Teknokratlar": {"satisfaction": 75}
        }
    },
    "Adalet ve Refah Partisi": {
        "ideology": "Muhafazakâr Demokrasi",
        "initial_resources": {
            "political_capital": 80,
            "cohesion": 75,
            "bureaucratic_efficiency": 50,
            "public_support": 70,
            "treasury": 150000
        },
        "factions": {
            "Gelenekçiler": {"satisfaction": 75},
            "Genç Kanat": {"satisfaction": 65},
            "Sosyal Destekçiler": {"satisfaction": 70}
        }
    },
    "Halkın Gücü Partisi": {
        "ideology": "Marksist-Sosyalist",
        "initial_resources": {
            "political_capital": 50,
            "cohesion": 85,
            "bureaucratic_efficiency": 30,
            "public_support": 45,
            "treasury": 50000
        },
        "factions": {
            "Sendikacılar": {"satisfaction": 75},
            "Öğrenciler": {"satisfaction": 60},
            "Parti Ortodoksları": {"satisfaction": 78}
        }
    },
    "Çevre ve Yeşil Yaşam Partisi": {
        "ideology": "Ekolojizm",
        "initial_resources": {
            "political_capital": 45,
            "cohesion": 70,
            "bureaucratic_efficiency": 60,
            "public_support": 55,
            "treasury": 75000
        },
        "factions": {
            "Radikal Aktivistler": {"satisfaction": 62},
            "Pragmatik Yeşiller": {"satisfaction": 75},
            "Toplum Gönüllüleri": {"satisfaction": 70}
        }
    },
    "Reform ve Teknoloji Partisi": {
        "ideology": "Teknokrasi",
        "initial_resources": {
            "political_capital": 55,
            "cohesion": 60,
            "bureaucratic_efficiency": 85,
            "public_support": 40,
            "treasury": 180000
        },
        "factions": {
            "İlericiler": {"satisfaction": 70},
            "Bürokratlar": {"satisfaction": 75},
            "Eğitimciler": {"satisfaction": 68}
        }
    },
    "Bölgesel Otonomi Cephesi": {
        "ideology": "Federalizm",
        "initial_resources": {
            "political_capital": 40,
            "cohesion": 80,
            "bureaucratic_efficiency": 45,
            "public_support": 65,
            "treasury": 90000
        },
        "factions": {
            "Yerel Temsilciler": {"satisfaction": 78},
            "Merkez Karşıtları": {"satisfaction": 72},
            "Kültürel Savunucular": {"satisfaction": 65}
        }
    },
    "Tarafsızlar Birliği": {
        "ideology": "Pragmatizm",
        "initial_resources": {
            "political_capital": 65,
            "cohesion": 50,
            "bureaucratic_efficiency": 75,
            "public_support": 50,
            "treasury": 120000
        },
        "factions": {
            "Anti-Politika": {"satisfaction": 60},
            "Esnek Çözümcüler": {"satisfaction": 75},
            "Ekonomik Realistler": {"satisfaction": 70}
        }
    }
}

# 10 Farklı Bölge ve Başlangıç Değerleri
# Hassasiyetler (0-100 aralığında) ve her partiye olan Doğal Çekim (ideolojik yakınlık)
REGIONS = {
    "Başkent Bölgesi": {
        "sensitivities": {"immigrant": 30, "inequality": 60, "polarization": 70},
        "natural_attraction": {
            "Ulusal Birlik Partisi": 15, "Özgürlük ve Demokrasi Hareketi": 20,
            "Adalet ve Refah Partisi": 25, "Halkın Gücü Partisi": 5,
            "Çevre ve Yeşil Yaşam Partisi": 10, "Reform ve Teknoloji Partisi": 15,
            "Bölgesel Otonomi Cephesi": 5, "Tarafsızlar Birliği": 5
        }
    },
    "Sanayi Metropolü": {
        "sensitivities": {"immigrant": 50, "inequality": 80, "polarization": 60},
        "natural_attraction": {
            "Ulusal Birlik Partisi": 10, "Özgürlük ve Demokrasi Hareketi": 25,
            "Adalet ve Refah Partisi": 15, "Halkın Gücü Partisi": 20,
            "Çevre ve Yeşil Yaşam Partisi": 5, "Reform ve Teknoloji Partisi": 15,
            "Bölgesel Otonomi Cephesi": 5, "Tarafsızlar Birliği": 5
        }
    },
    "Tarım Havzası": {
        "sensitivities": {"immigrant": 60, "inequality": 40, "polarization": 40},
        "natural_attraction": {
            "Ulusal Birlik Partisi": 20, "Özgürlük ve Demokrasi Hareketi": 5,
            "Adalet ve Refah Partisi": 30, "Halkın Gücü Partisi": 15,
            "Çevre ve Yeşil Yaşam Partisi": 10, "Reform ve Teknoloji Partisi": 5,
            "Bölgesel Otonomi Cephesi": 10, "Tarafsızlar Birliği": 5
        }
    },
    "Turizm Cenneti": {
        "sensitivities": {"immigrant": 20, "inequality": 50, "polarization": 50},
        "natural_attraction": {
            "Ulusal Birlik Partisi": 10, "Özgürlük ve Demokrasi Hareketi": 30,
            "Adalet ve Refah Partisi": 20, "Halkın Gücü Partisi": 5,
            "Çevre ve Yeşil Yaşam Partisi": 15, "Reform ve Teknoloji Partisi": 10,
            "Bölgesel Otonomi Cephesi": 5, "Tarafsızlar Birliği": 5
        }
    },
    "Akademik Şehir": {
        "sensitivities": {"immigrant": 10, "inequality": 70, "polarization": 80},
        "natural_attraction": {
            "Ulusal Birlik Partisi": 5, "Özgürlük ve Demokrasi Hareketi": 25,
            "Adalet ve Refah Partisi": 10, "Halkın Gücü Partisi": 20,
            "Çevre ve Yeşil Yaşam Partisi": 20, "Reform ve Teknoloji Partisi": 15,
            "Bölgesel Otonomi Cephesi": 0, "Tarafsızlar Birliği": 5
        }
    },
    "Geleneksel Kale": {
        "sensitivities": {"immigrant": 70, "inequality": 30, "polarization": 30},
        "natural_attraction": {
            "Ulusal Birlik Partisi": 30, "Özgürlük ve Demokrasi Hareketi": 5,
            "Adalet ve Refah Partisi": 40, "Halkın Gücü Partisi": 5,
            "Çevre ve Yeşil Yaşam Partisi": 5, "Reform ve Teknoloji Partisi": 0,
            "Bölgesel Otonomi Cephesi": 10, "Tarafsızlar Birliği": 5
        }
    },
    "Sınır Ticareti Bölgesi": {
        "sensitivities": {"immigrant": 80, "inequality": 60, "polarization": 50},
        "natural_attraction": {
            "Ulusal Birlik Partisi": 25, "Özgürlük ve Demokrasi Hareketi": 10,
            "Adalet ve Refah Partisi": 20, "Halkın Gücü Partisi": 10,
            "Çevre ve Yeşil Yaşam Partisi": 5, "Reform ve Teknoloji Partisi": 5,
            "Bölgesel Otonomi Cephesi": 20, "Tarafsızlar Birliği": 5
        }
    },
    "Madencilik Yöresi": {
        "sensitivities": {"immigrant": 50, "inequality": 90, "polarization": 60},
        "natural_attraction": {
            "Ulusal Birlik Partisi": 15, "Özgürlük ve Demokrasi Hareketi": 5,
            "Adalet ve Refah Partisi": 20, "Halkın Gücü Partisi": 35,
            "Çevre ve Yeşil Yaşam Partisi": 5, "Reform ve Teknoloji Partisi": 5,
            "Bölgesel Otonomi Cephesi": 10, "Tarafsızlar Birliği": 5
        }
    },
    "Teknoloji Geliştirme Bölgesi": {
        "sensitivities": {"immigrant": 20, "inequality": 40, "polarization": 70},
        "natural_attraction": {
            "Ulusal Birlik Partisi": 5, "Özgürlük ve Demokrasi Hareketi": 35,
            "Adalet ve Refah Partisi": 10, "Halkın Gücü Partisi": 5,
            "Çevre ve Yeşil Yaşam Partisi": 10, "Reform ve Teknoloji Partisi": 30,
            "Bölgesel Otonomi Cephesi": 0, "Tarafsızlar Birliği": 5
        }
    },
    "Özerk Kültür Bölgesi": {
        "sensitivities": {"immigrant": 40, "inequality": 50, "polarization": 40},
        "natural_attraction": {
            "Ulusal Birlik Partisi": 5, "Özgürlük ve Demokrasi Hareketi": 15,
            "Adalet ve Refah Partisi": 10, "Halkın Gücü Partisi": 15,
            "Çevre ve Yeşil Yaşam Partisi": 10, "Reform ve Teknoloji Partisi": 5,
            "Bölgesel Otonomi Cephesi": 35, "Tarafsızlar Birliği": 5
        }
    }
}
