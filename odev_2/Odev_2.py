class Film:
    def __init__(self, filmAdı, filmYılı, yonetmen, tur):
        self.filmAdı = filmAdı
        self.filmYılı = filmYılı
        self.yonetmen = yonetmen
        self.tur = tur

    def __str__(self):
        return f"{self.filmAdı} ({self.filmYılı}), Yönetmen: {self.yonetmen}, Tür: {self.tur}"


def film_ekle():
    filmAdı = input("Film adını girin: ")
    filmYılı = input("Film yılını girin: ")
    yonetmen = input("Yönetmeni girin: ")
    tur = input("Film türünü girin: ")

    film = Film(filmAdı, filmYılı, yonetmen, tur)

    with open("filmler.txt", "a") as file:
        file.write(f"{filmAdı},{filmYılı},{yonetmen},{tur}\n")

    print("Film başarıyla eklendi.")


def film_sil():
    silinecek_film = input("Silinecek film adını girin: ")

    with open("filmler.txt", "r") as file:
        filmler = file.readlines()

    with open("filmler.txt", "w") as file:
        for film in filmler:
            if film.split(",")[0] != silinecek_film:
                file.write(film)

    print("Film başarıyla silindi.")


def film_ara():
    aranan_film = input("Aranacak film adını girin: ")

    with open("filmler.txt", "r") as file:
        filmler = file.readlines()

    bulunan_filmler = []
    for film in filmler:
        if aranan_film.lower() in film.lower():
            bulunan_filmler.append(film)

    if bulunan_filmler:
        print("Bulunan filmler:")
        for film in bulunan_filmler:
            film_bilgileri = film.strip().split(",")
            filmAdı = film_bilgileri[0]
            filmYılı = film_bilgileri[1]
            yonetmen = film_bilgileri[2]
            tur = film_bilgileri[3]
            print(Film(filmAdı, filmYılı, yonetmen, tur))
    else:
        print("Aradığınız film bulunamadı.")


while True:
    print("\n--- Film Kütüphanesi ---")
    print("1. Filmleri listele")
    print("2. Film ekle")
    print("3. Film sil")
    print("4. Film ara")
    print("5. Çıkış")

    secim = input("Bir seçenek girin (1-5): ")

    if secim == "1":
        with open("filmler.txt", "r") as file:
            filmler = file.readlines()

        if filmler:
            print("Mevcut filmler:")
            for film in filmler:
                film_bilgileri = film.strip().split(",")
                filmAdı = film_bilgileri[0]
                filmYılı = film_bilgileri[1]
                yonetmen = film_bilg
                
                men = film_bilgileri[2]
                tur = film_bilgileri[3]
                print(Film(filmAdı, filmYılı, yonetmen, tur))
        else:
                  print("Kütüphane boş.")
    elif secim == "2":
                  film_ekle()
    elif secim == "3":
                  film_sil()
        
    elif secim == "4":
                  film_ara()
                
    elif secim == "5":
                  print("Program sonlandırılıyor...")
              