'İlk olarak kaç adım sayı gösterileceğini soruyoruz.'
sayi = int(input("Kaç adım listelenecek: "))
if sayi > 2: # İstenilen adım sayısı 2'den yüksek olmadıkça hesaplamaya ihtiyaç duyulmuyor.
    ilk, son = 1,1
    print("1,1",end="")     #Sırayla ilk iki sayıyı ekrana basıyoruz. Bunlar için bir işleme gerek yok.
    for i in range(sayi):   #İstenilen adım kadar döngü çalışıyor.
        gecici = son        # ilk ve son değişkenleri arasında değer aktarımı olacağı için gecici adında üçüncü bir değişkene ihtiyaç duyuyoruz.
        son += ilk
        ilk = gecici
        print(","+str(son),end="") # String ile ancak string toplanabileceğinden sayıyı stringe dönüştürüyoruz ve ekrana basıyoruz.
    print()
else:
    print("Dizinin ilk iki sayısı 1 ve 1'dir.")
