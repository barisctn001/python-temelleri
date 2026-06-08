class Uye:
    def __init__(self, isim, eposta):
        self.isim = isim
        self.eposta = eposta


class Ogrenci(Uye):
    def __init__(self, isim, eposta, okul_numarasi):


        super().__init__(isim, eposta)
        self.okul_numarasi = 1907

Ogrenci1 = Ogrenci("Barış çetin", "bariscetin2008Qgmail.com", 1907)

print(f"üye adı: {Ogrenci1.isim}")
print(f"E-posta: {Ogrenci1.eposta}")
print(f"okul numarasi: {Ogrenci1.okul_numarasi}")
