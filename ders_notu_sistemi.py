class dersnotu:
    def __init__(self, isim, vize, final):
       self.isim = isim
       self.vize = vize
       self.final = final

    def durum_kontrol(self):
       ortalama = (self.vize + self.final) / 2

       if ortalama >= 50:
           print(f"{self.isim} bu dersi {ortalama} ortalama ile geçti")

       else:
           print(f"{self.isim} bu dersten {ortalama} ortalama ile KALDI")


isim1 = dersnotu("barış çetin", 70, 80)
isim2 = dersnotu("ahmet yılmaz", 40, 90)

isim1.durum_kontrol()
isim2.durum_kontrol()
