from arac import MetrobusAraci
from log import LogManager

class Merkez:
    def __init__(self):
        self.arac_listesi = []
        self.atanan_arac = {}
        self.log = LogManager("Merkez")

    def arac_ekle(self, arac_id):
        yeni_arac = MetrobusAraci(arac_id)
        self.arac_listesi.append(yeni_arac)

    def durak_raporla(self, rapor):
        durak = rapor["durak"]
        seviye = rapor["kalabalik_seviyesi"]

        if seviye > 7:
            self.log.alert(f"Yüksek kalabalık tespit edildi: {durak} - Araç yönlendiriliyor...")
            self.arac_gonder(durak)
        elif 4 <= seviye <= 7:
            self.log.warning(f"Orta kalabalık: {durak} - Bekleniyor...")
        else:
            self.log.info(f"Normal kalabalık: {durak}")

    def arac_gonder(self, durak_adi):
        for arac in self.arac_listesi:
            if arac.durum == "boşta":
                arac.goreve_basla(durak_adi)
                self.atanan_arac[durak_adi] = arac.arac_id
                self.log.success(f" {arac.arac_id}, {durak_adi} durağına yönlendirildi.")
                return

        self.log.error("❌ Uygun araç bulunamadı!")

    def durak_raporla_kaynak_ile(self, rapor, kaynak_durak):
        durak = rapor["durak"]
        seviye = rapor["kalabalik_seviyesi"]

        if seviye > 7:
            self.log.alert(f"Yüksek kalabalık tespit edildi: {durak}")
            self.log.info(f" {kaynak_durak} durağından {durak} durağına araç yönlendiriliyor...")
            self.arac_gonder_kaynak_ile(durak, kaynak_durak)
        elif 4 <= seviye <= 7:
            self.log.warning(f"Orta kalabalık: {durak} - İzleniyor...")
        else:
            self.log.info(f"Normal kalabalık: {durak}")

    def arac_gonder_kaynak_ile(self, hedef_durak, kaynak_durak):
        for arac in self.arac_listesi:
            if arac.durum == "boşta":
                arac.goreve_basla_kaynak_ile(hedef_durak, kaynak_durak)
                self.atanan_arac[hedef_durak] = arac.arac_id
                self.log.success(f" {arac.arac_id}, {kaynak_durak} → {hedef_durak} rotasına yönlendirildi.")
                return

        self.log.error("❌ Uygun araç bulunamadı!")
