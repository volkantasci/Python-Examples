from os import system
kitaplar = list()

menu = """
[1] Kitap Ara
[2] Yazar Ara
[3] Kitap Çıkar
[4] Kitap Ekle
[5] Kitapları Görüntüle
[Q] Çıkış

"""

def kitapListele(liste:str):
	for i in liste:
		print("Yazar: {}   Kitap: {}".format(i[0], i[1]))
	input("Ana menüye dönmek için 'enter'e bas!")
	
	


def kitapAra(kitapAdi:str):
	kitapAdi = kitap.lower()
	newList = list()
	for i in kitaplar:
		if kitapAdi == i[1]:
			newList.append(i)
	
	if newList:
		print(len(newList),"adet kitap bulundu.")
	else:
		print("Kitap bulunamadı.")

	input("Ana menüye dönmek için 'enter'e bas!")



def yazarAra(yazar:str):
	yazar = yazar.lower()
	newList = list()
	for i in kitaplar:
		if yazar == i[0]:
			newList.append(i)
	if newList:
		print("Yazara ait {} adet kitap bulundu!")
		kitapListele(newList)
	else:
		print("Yazara ait kitap bulunamadı!")
		input("Ana menüye dönmek için 'enter'e bas!")


def kitapCikar(kitapAdi:str):
	kitapAdi = kitapAdi.lower()
	flag = False
	newList = list()
	for i in kitaplar:
		if kitapAdi == i[1]:
			flag = True
			newList.append(i)

	if flag:
		for x,kitap in enumerate(newList):
			print(x+1, '--->', "Yazar: {}   Kitap Adı: {}".format(kitap[0], kitap[1]))

		secim = int(input("Çıkartılacak Kitabı Seçin: "))
		while secim <= 0 or secim > len(newList):
			print("Hatalı giriş! Liste içerisinde bu sayı yok!")
			secim = int(input("Çıkartılacak Kitabı Seçin: "))

		kitaplar.remove(newList[secim-1])
		print("Kitap Çıkartıldı!")



	if flag == False:
		print("Böyle bir kitap bulunamadı!")
		input("Ana menüye dönmek için 'enter'e bas!")

	input("Ana menüye dönmek için 'enter'e bas!")



def kitapEkle():
	yazar = input("Yazar Adı: ")
	yazar = yazar.lower()
	kitapAdi = input("Kitap Adı: ")
	kitapAdi = kitapAdi.lower()
	kitap = (yazar,kitapAdi)
	kitaplar.append(kitap)
	print("Kitap Eklendi!")
	input("Ana menüye dönmek için 'enter'e bas!")



while True:
	system("clear") #Eğer Windows kullanıyorsanız buraya 'cls' yazın. Ekranı temizlemek için kullanıyoruz.
	print(menu)
	giris = input("Seçim: ")

	if giris == "1":
		kitap = input("Aranan Kitap: ")
		kitapAra(kitap)

	elif giris == "2":
		yazar = input("Aranan Yazar: ")
		yazarAra(yazar)

	elif giris == "3":
		kitap = input("Çıkartılacak Kitap: ")
		kitapCikar(kitap)

	elif giris == "4":
		kitapEkle()

	elif giris == "5":
		kitapListele(kitaplar)
		

	elif giris == "Q" or giris == "q":
		print("Çıkılıyor...")
		quit()

	else:
		print("Hatalı Giriş!")
