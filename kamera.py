import random
from log import LogManager

class KalabalikKamera:
    def __init__(self, durak_adi, kaynak=0):
        self.durak_adi = durak_adi
        self.kaynak = kaynak
        self.log = LogManager("KalabalikKamera")

    def kalabalik_tespit_et(self):
        person_count = random.randint(0, 50)
        self.log.info(f"{self.durak_adi} - Tespit edilen kişi sayısı: {person_count}")
        return person_count
