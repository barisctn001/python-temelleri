import tkinter as tk
from pydoc import text
from tkinter import font

pencere = tk.Tk()
pencere.title("şükrü saraçoğlu protokol girişi")
pencere.geometry("500x400")

def giris_yap():

    uyarı.config(text="Giriş Başarılı! koltuk numarası: blok 1907")

uyarı = tk.Label(pencere, text="Protokol girişi için lütfen bilgilerinizi kontrol ediniz.", font=("arial", 12 ))
uyarı.pack(pady=20)


buton = tk.Button(pencere, text="Bileti okut ve giriş yap.", font=("arial", 12, "bold"), bg="navy", fg="white", command=giris_yap)
buton.pack(pady=20)

pencere.mainloop()
