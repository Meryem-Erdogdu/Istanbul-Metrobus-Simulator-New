# Istanbul-Metrobus-Simulator-New
Bu proje, Bilgisayar Ağ Sistemleri dersi kapsamında geliştirilmiştir. İstanbul'daki metrobüs sistemini simüle eden, her duraktaki rastgele kalabalık tespiti yapan ve buna göre metrobüs araçlarını yönlendiren bir sistemdir. Tamamen Nesne Tabanlı Programlama (OOP) ile yazılmıştır ve CSV dosyasına bağımlılık olmadan çalışır. Tüm veriler rastgele üretilir ve gerçek zamanlı olarak loglanır.

Özellikler

- Kalabalık Tespiti : Her durakta bir kamera nesnesi vardır. Bu kamera, rastgele sayılarla kalabalığı simüle eder.
- NVR Cihazı : Kamera verisini alır ve Merkez'e iletir.
- Merkez Kontrol Sistemi : Gelen raporlara göre yüksek kalabalık tespit edilen duraklara boşta olan metrobüsleri yönlendirir.
- Loglama Sistemi : Tüm işlemler INFO, WARNING, ERROR, SUCCESS gibi seviyelerde loglanır.
- Random Veri Üretimi : Gerçek bir CSV dosyasına gerek yoktur. Rastgele oluşturulan durak verisi ile çalışır.
- Modüler Yapı : Her sınıf ayrı bir dosyada olup, sistemin farklı bileşenleri arasında haberleşme sağlanır.

# Nasıl Çalışıyor Peki ?

![Ekran görüntüsü 2025-06-08 210152](https://github.com/user-attachments/assets/44f60469-7379-4566-9b18-5ea3d417bd2d)


![Ekran görüntüsü 2025-06-08 210211](https://github.com/user-attachments/assets/1665f046-110b-4141-95c1-4c0bb280a5da)


![Ekran görüntüsü 2025-06-08 210226](https://github.com/user-attachments/assets/6e4d52bf-f288-4776-a523-27d22d5b691e)

‼️
- Tek durak seçerken: 9
- Çoklu durak seçerken : 5,14,35
- Çıkış için: q
