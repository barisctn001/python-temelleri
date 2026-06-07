class ogrenci:
    def __init__(self, ogrenci, sınıf):
      self.ogrenci = ogrenci
      self.sınıf = sınıf


ogrenci_listesi = []


def ogrenci_ekle(yeni_ogrenci):
   global ogrenci_listesi
   ogrenci_listesi.append(yeni_ogrenci)


   print(f"{yeni_ogrenci.ogrenci} sisteme başarıyla kaydedildi")



ogrenci1 = ogrenci("barış çetin", "12-A")
ogrenci2 = ogrenci("ahmet", "12-B")


ogrenci_ekle(ogrenci1)
ogrenci_ekle(ogrenci2)
