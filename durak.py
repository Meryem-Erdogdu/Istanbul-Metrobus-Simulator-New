class Durak:
    def __init__(self, kod, ad, enlem, boylam):
        self.kod = kod
        self.ad = ad
        self.enlem = enlem
        self.boylam = boylam

    def __str__(self):
        return f"{self.ad} ({self.kod})"
