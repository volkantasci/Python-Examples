sayi = 1 # döngünğn başlangıcı için sayı değişkenine ilk olarak 1 değerini veriyoruz.
toplam = 0 # toplama işlemi sonuçları için bir toplam değişkeni oluşturuyoruz.

while sayi != 0: # DÖngümüz burada başlıyor, eğer kullanıcı 0 girerse sayı değişkenine döngümğz tekrar etmeyecektir.
    sayi = float(input("Sayı: ")) # Kullanıcımızdan sayı istiyoruz.
    toplam += sayi # alınan her sayı toplam değişkeninin üzerine ekleniyor.
    print("Toplam:",toplam) #İşlemlerden sonra toplam sonucu ekrana basılıyor.
