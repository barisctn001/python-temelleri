sepet = []


def urun_ekle(urun_adi):
    global sepet
    sepet.append(urun_adi)
    print(urun_adi, "sepete eklendi!")

def sepeti_goster():
    global sepet
    print("\n--- SEPETİNİZDEKİ ÜRÜNLER ---")
    for urun in sepet:
        print(urun)

urun_ekle("cips")
urun_ekle("kola")
urun_ekle("muz")

sepeti_goster()
