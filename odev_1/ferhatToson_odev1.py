# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BNh9eV8eLyuvBZFVXPjx6yk_1PDRw54i
"""

def bilgi_kaydet():
    kullanici_adi = input("Kullanıcı adınızı girin: ")
    sifre = input("Şifrenizi girin: ")

    with open("kullanici_bilgileri.txt", "a") as dosya:
        dosya.write(kullanici_adi + "," + sifre + "\n")
def giris():
    kullanici_adi = input("Kullanıcı adınızı giriniz: ")
    sifre = input("Şifrenizi giriniz: ")

    with open("kullanici_bilgileri.txt", "r") as dosya:
        for satir in dosya:
            bilgiler = satir.strip().split(",")
        if bilgiler[0] == kullanici_adi and bilgiler[1] == sifre:
                print("Giriş yapıldı.")
        else:
               print("Kullanıcı adı veya şifre yanlış.")
bilgi_kaydet()
giris()