sayi = int(input("Sayı: ")) # Kullanıcıdan bir sayı istiyoruz ve bu sayıyı tamsayıya çeviriyoruz. Aksi takdirde sayısal işlem yapamayız.
toplam = 1 # Çarpma işleminin etkisiz elemanı olan 1 sayısı ile başlatıyoruz çarpım işlemlerini.
for i in range(2,sayi+1): # range fonksiyonu ile 2'den başlayı sayı+1'e kadar (sayı+1 dahil değil) olan sayıları
    toplam *= i           # i değişkenine aktarıyoruz ve bu sayıları çarparak toplam değişkenine atıyoruz.

print("Sonuç:",toplam)  # Son olarak da çarpımların sonucunu ekrana basıyoruz.
