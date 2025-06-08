from log import LogManager

class NVR:
    def __init__(self, durak_kamera):
        self.kamera = durak_kamera
        self.log = LogManager("NVR")

    def veri_al_ve_gonder(self):
        seviye = self.kamera.kalabalik_tespit_et()
        self.log.info(f"{self.kamera.durak_adi} - NVR cihazından veri gönderildi: {seviye}")
        return {
            "durak": self.kamera.durak_adi,
            "kalabalik_seviyesi": seviye
        }
