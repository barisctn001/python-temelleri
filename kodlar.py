# =====================================================================
#             BARIŞ ÇETİN - PYTHON ÖĞRENME GÜNLÜĞÜ İLK KODLAR
# =====================================================================

print("--- 1. BÖLÜM: LİSTELER VE İNDEKS MANTIĞI ---")
# İlk oluşturduğun en sevdiğin yemekler listesi
# Python saymaya 0'dan başladığı için 1. indeks bize 'çorba'yı verir.
yemekler = ["mantı", "çorba", "iskender"]
print("Listenin ikinci elemanı (1. indeks):", yemekler[1])


print("\n--- 2. BÖLÜM: LİSTEYE ELEMAN EKLEME VE SİLME ---")
# Listeye .append() ile 'puding' ekledik, .remove() ile 'çorba'yı sildik
yemekler.append("puding")
yemekler.remove("çorba")
print("Ekleme ve silme işlemlerinden sonra listenin son hali:")
print(yemekler)


print("\n--- 3. BÖLÜM: FOR DÖNGÜSÜ VE IF ŞARTININ BİRLEŞİMİ ---")
# range(1, 11) ile 1'den 10'a kadar olan çift sayıları filtreleyip bastık
print("1 ile 10 arasındaki çift sayılar:")
for sayi in range(1, 11):
    if sayi % 2 == 0:
        print(sayi)


print("\n--- 4. BÖLÜM: WHILE DÖNGÜSÜ İLE GERİ SAYIM ---")
# Şart doğru olduğu sürece dönen ve sonsuz döngüye girmeyen geri sayımımız
geri_sayim = 5
print("Geri sayım başladı:")
while geri_sayim > 0:
    print(geri_sayim)
    geri_sayim = geri_sayim - 1


print("\n--- 5. BÖLÜM: FONKSİYONLAR (TEMBELLİĞİN ZİRVESİ) ---")
# Parametre alan ve güvenli bir şekilde int dönüşümü yapan toplama fonksiyonun
def toplama_yap(a, b):
    print("Toplama Sonucu:", int(a) + int(b))

# Fonksiyonu çağırıp düğmeye basıyoruz
toplama_yap(5, 10)

print("\n=====================================================================")
print("Bu dosyadaki tüm kodlar Barış Çetin tarafından başarıyla yazılmıştır!")
print("=====================================================================")
