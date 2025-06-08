import time
import random
import threading
from merkez import Merkez
from kamera import KalabalikKamera
from nvr import NVR
from veri import durak_verisini_yukle, onceki_durak_bul, durak_bilgisi_getir, kisi_sayisi_uret, kalabalik_seviyesi_belirle
from log import LogManager

def durak_secim_menusu(duraklar):
    print("\n" + "="*80)
    print(" METROBüS DURAK SEÇİM SİSTEMİ - CANLI İZLEME")
    print("="*80)
    
    for i, durak in enumerate(duraklar, 1):
        print(f"{i:2d}. {durak['DURAK_ADI']}")
    
    print("="*80)
    
    while True:
        try:
            secim = input(f"\nDurak seçin (1-{len(duraklar)}) veya 'q' çıkış: ").strip()
            
            if secim.lower() == 'q':
                return None
                
            secilen_duraklar = []
  
            if ',' in secim:
                secimler = secim.split(',')
                for s in secimler:
                    secim_no = int(s.strip())
                    if 1 <= secim_no <= len(duraklar):
                        secilen_duraklar.append(duraklar[secim_no - 1])
                    else:
                        print(f"❌ Geçersiz seçim: {secim_no}")
                        return durak_secim_menusu(duraklar)
    
            elif '-' in secim and secim.count('-') == 1:
                baslangic, bitis = secim.split('-')
                baslangic = int(baslangic.strip())
                bitis = int(bitis.strip())
                
                if 1 <= baslangic <= len(duraklar) and 1 <= bitis <= len(duraklar) and baslangic <= bitis:
                    for i in range(baslangic, bitis + 1):
                        secilen_duraklar.append(duraklar[i - 1])
                else:
                    print("❌ Geçersiz aralık! Lütfen doğru aralık girin (örn: 5-10)")
                    continue
   
            else:
                secim_no = int(secim)
                if 1 <= secim_no <= len(duraklar):
                    secilen_duraklar.append(duraklar[secim_no - 1])
                else:
                    print("❌ Geçersiz seçim! Lütfen doğru aralıkta bir sayı girin.")
                    continue
            
            return secilen_duraklar
            
        except ValueError:
            print("❌ Lütfen geçerli bir sayı girin!")

def durak_bilgilerini_goster(duraklar):
 
    print("\n" + "="*80)
    print(" DURAK BİLGİLERİ")
    print("="*80)
    
    for durak in duraklar:
        kisi_sayisi = durak['KISI_SAYISI']
        seviye = durak['KALABALIK_SEVIYESI']
        
        print(f"Durak Adı: {durak['DURAK_ADI']}")
        print(f"Durak Kodu: {durak['DURAK_KODU']}")
        print(f"Konum: {durak['ENLEM']}, {durak['BOYLAM']}")
        print(f"Kalabalık: {seviye} ({kisi_sayisi} kişi)")
        print("-" * 50)
    
    print("="*80)

def durak_verilerini_guncelle(duraklar):
   
    for durak in duraklar:
        yeni_kisi_sayisi = kisi_sayisi_uret()
        seviye, ikon = kalabalik_seviyesi_belirle(yeni_kisi_sayisi)
        durak['KISI_SAYISI'] = yeni_kisi_sayisi
        durak['KALABALIK_SEVIYESI'] = seviye
        durak['SEVIYE_IKONU'] = ikon

def canli_izleme_baslat(secilen_duraklar, duraklar, merkez):
    log = LogManager("Canlı İzleme")
    
    print("\nCANLI İZLEME BAŞLATILDI")
    print("Durdurmak için Ctrl+C tuşlarına basın")
    print("="*80)
    
    try:
        while True:
            durak_verilerini_guncelle(duraklar)
            
            print("\033[2J\033[1;1H", end="")  
            
            print(f"\n {time.strftime('%H:%M:%S')} - CANLI DURAK TAKİBİ")
            print("="*80)
            
            for durak in secilen_duraklar:
                güncel_durak = next((d for d in duraklar if d['DURAK_KODU'] == durak['DURAK_KODU']), durak)
                
                kisi_sayisi = güncel_durak['KISI_SAYISI']
                seviye = güncel_durak['KALABALIK_SEVIYESI']
                
                print(f" {güncel_durak['DURAK_ADI']:<35} {seviye} ({kisi_sayisi} kişi)")
                
                if kisi_sayisi > 65:
                    onceki_durak = onceki_durak_bul(güncel_durak["DURAK_ADI"], duraklar)
                    if onceki_durak:
                        rapor = {
                            "durak": güncel_durak["DURAK_ADI"],
                            "kalabalik_seviyesi": 9  
                        }
                        merkez.durak_raporla_kaynak_ile(rapor, onceki_durak["DURAK_ADI"])
            
            print("="*80)
            print(" Durdurmak için Ctrl+C tuşlarına basın")
            
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\n\n Canlı izleme durduruldu.")
        return

def metrobus_yonlendir(hedef_durak, kaynak_durak, merkez):

    log = LogManager("Yönlendirme")
    
    print(f"\n METROBüS YÖNLENDİRME")
    print("="*50)
    print(f" Kaynak Durak: {kaynak_durak['DURAK_ADI']}")
    print(f" Hedef Durak: {hedef_durak['DURAK_ADI']}")
    print("="*50)
    
    log.info(f"Metrobüs yönlendirme başlatılıyor...")
    log.info(f"Kaynak: {kaynak_durak['DURAK_ADI']} → Hedef: {hedef_durak['DURAK_ADI']}")
    
    kisi_sayisi = hedef_durak['KISI_SAYISI']
    if kisi_sayisi > 65:
        seviye = 9
    elif kisi_sayisi > 35:
        seviye = 6
    else:
        seviye = 3
    
    rapor = {
        "durak": hedef_durak["DURAK_ADI"],
        "kalabalik_seviyesi": seviye
    }
    
    merkez.durak_raporla_kaynak_ile(rapor, kaynak_durak["DURAK_ADI"])

def simulasyon():
    log = LogManager("Simulasyon")
    log.info(" Metrobüs Kalabalık Yönetim Sistemi Başlatılıyor...")
    
    duraklar = durak_verisini_yukle()
    log.info(f" {len(duraklar)} durak yüklendi.")
    
    merkez = Merkez()
    
    for i in range(1, 6):
        merkez.arac_ekle(f"MB-{i:03d}")
    
    while True:
        print("\nMETROBüS YÖNETİM SİSTEMİ - GELİŞMİŞ İZLEME")
        
        secilen_duraklar = durak_secim_menusu(duraklar)
        
        if secilen_duraklar is None:  
            log.success(" Sistem kapatılıyor...")
            break
        
        durak_bilgilerini_goster(secilen_duraklar)
        
        print("\n SEÇENEKLER:")
        print("1.  Canlı izleme başlat")
        print("2.  Metrobüs yönlendir")
        print("3. Yeni durak seçimi")
        
        secim = input("\nSeçiminizi yapın (1-3): ").strip()
        
        if secim == "1":
            canli_izleme_baslat(secilen_duraklar, duraklar, merkez)
        
        elif secim == "2":
            for durak in secilen_duraklar:
                onceki_durak = onceki_durak_bul(durak["DURAK_ADI"], duraklar)
                if onceki_durak:
                    print(f"\n Önceki durak: {onceki_durak['DURAK_ADI']}")
                    metrobus_yonlendir(durak, onceki_durak, merkez)
                else:
                    log.error(f"❌ {durak['DURAK_ADI']} için önceki durak bulunamadı!")
        
        elif secim == "3":
            continue
        
        else:
            print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    simulasyon()
