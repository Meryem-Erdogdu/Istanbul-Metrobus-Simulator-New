import random

def kisi_sayisi_uret():
    return random.randint(0, 100)

def kalabalik_seviyesi_belirle(kisi_sayisi):
    if kisi_sayisi <= 35:
        return "Düşük", "🟢"
    elif kisi_sayisi <= 65:
        return "Orta", "🟡"
    else:
        return "Çok", "🔴"

def durak_verisini_yukle():
    gercek_duraklar = [
        "Beylikdüzü Sondurak", "Beykent", "Cumhuriyet Mahallesi", "Beylikdüzü Belediye",
        "Beylikdüzü", "Güzelyurt", "Haramidere", "Haramidere Sanayi", "Saadetdere Mahallesi",
        "Mustafa Kemalpaşa", "Cihangir – Üniversite Mahallesi", "Avcılar Merkez Üniversite Kampüsü",
        "Şükrübey", "Büyükşehir Belediye Sosyal Tesisleri", "Küçükçekmece", "Cennet Mahallesi",
        "Florya", "Beşyol", "Sefaköy", "Yenibosna", "Bahçelievler", "İncirli", "Zeytinburnu",
        "Merter", "Cevizlibağ", "Topkapı", "Bayrampaşa", "Edirnekapı", "Otogar", "Esenler",
        "Menderes", "Gaziosmanpaşa", "Eyüpsultan", "Alibeyköy", "Okmeydanı", "Çağlayan",
        "Halıcıoğlu", "Kemerburgaz", "Levent", "Etiler", "Akatlar", "Mecidiyeköy", "Zincirlikuyu",
        "Gayrettepe", "Beşiktaş", "Barbaros", "Balmumcu", "Nişantaşı"
    ]

    duraklar = []
    for i, ad in enumerate(gercek_duraklar, start=1001):
        enlem = round(random.uniform(40.9000, 41.1000), 4)
        boylam = round(random.uniform(28.5000, 29.1000), 4)
        kisi_sayisi = kisi_sayisi_uret()
        seviye, ikon = kalabalik_seviyesi_belirle(kisi_sayisi)
        duraklar.append({
            "DURAK_KODU": i,
            "DURAK_ADI": ad,
            "ENLEM": enlem,
            "BOYLAM": boylam,
            "SIRALAMA": i - 1000,
            "KISI_SAYISI": kisi_sayisi,
            "KALABALIK_SEVIYESI": seviye,
            "SEVIYE_IKONU": ikon
        })

    return duraklar

def onceki_durak_bul(hedef_durak_adi, duraklar):
    for i, durak in enumerate(duraklar):
        if durak["DURAK_ADI"] == hedef_durak_adi:
            if i > 0:
                return duraklar[i-1]
            else:
                return duraklar[-1]
    return None

def durak_bilgisi_getir(durak_adi, duraklar):
    for durak in duraklar:
        if durak["DURAK_ADI"] == durak_adi:
            return durak
    return None
