from log import LogManager
from time import sleep

class MetrobusAraci:
    def __init__(self, arac_id):
        self.arac_id = arac_id
        self.durum = "boşta"
        self.hedef_durak = None
        self.log = LogManager("Araç")

    def goreve_basla(self, durak_adi):
        self.durum = "göreve gidiyor"
        self.hedef_durak = durak_adi
        self.log.info(f"{self.arac_id} - Göreve başlıyor: {self.hedef_durak}")
        self._seyahat_simulasyonu()

    def goreve_basla_kaynak_ile(self, hedef_durak, kaynak_durak):
        self.durum = "göreve gidiyor"
        self.hedef_durak = hedef_durak
        self.kaynak_durak = kaynak_durak
        self.log.info(f"{self.arac_id} - Rota: {self.kaynak_durak} → {self.hedef_durak}")
        self._seyahat_simulasyonu_kaynak_ile()

    def _seyahat_simulasyonu(self):
        self.log.info(f"{self.arac_id} - {self.hedef_durak} yönünde hareket ediyor...")
        sleep(2)
        self.durum = "hizmet veriyor"
        self.log.success(f"{self.arac_id} - {self.hedef_durak} durağına ulaştı.")
        sleep(1)
        self.durum = "boşta"
        self.log.info(f"{self.arac_id} - Görev tamamlandı. Durum: boşta")

    def _seyahat_simulasyonu_kaynak_ile(self):
        self.log.info(f"{self.arac_id} - {self.kaynak_durak} durağından hareket ediyor...")
        sleep(1)
        self.log.info(f"{self.arac_id} - {self.hedef_durak} yönünde ilerliyor...")
        sleep(2)
        self.durum = "hizmet veriyor"
        self.log.success(f"{self.arac_id} - {self.hedef_durak} durağına ulaştı.")
        sleep(1)
        self.durum = "boşta"
        self.log.success(f"{self.arac_id} - Görev tamamlandı. Durum: boşta")
