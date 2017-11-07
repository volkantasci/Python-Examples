alfabe = "abcçdefgğhıijklmnoöprsştuüvyz.;' abcçdefgğhıijklmnoöprsştuüvyz.;' "
# Alfabeyi iki kez yazdık çünkü biz bir harf arattığımızda ilk bulduğu index'i baz alarak işlem yapacak.
# Ancak ben alfabedeki son karakteri istersem 3 fazlası olan karakteri almak isterken hata verecek.
# Bunun yerine son karakterden sonra başa dönmüş gibi ilerleyecek ve 3 ileriki karakterin index'ini verecek.

textInput = input("Metin: ")

textInput = textInput.lower() # Bu kısımda kullanıcının girdiği text ifadeyi tamamen küçük harflere dönüştürdük.

newText = ""
for i in textInput:
    x = alfabe.index(i) + 3
    newText += alfabe[x] # Yeni text burada oluşturuluyor.

print("Şifrelendi:",newText)

"""
Bu kısım ise şifrelenmiş metni geri düzeltmek için. Eğer bu kısmı aktif ederseniz şifrelenen bir metin isteyecek
ve girdiğiniz şifrelenmiş metni normal okunabilir hale getirecek.
Kod Aşağıda:


textInput = input("Metin: ")
textInput = textInput.lower() # Bu kısımda kullanıcının girdiği text ifadeyi tamamen küçük harflere dönüştürdük.

newText = ''

for i in textInput:
    x = alfabe.index(i) - 3
    newText += alfabe[x] # Okunabilir text burada oluşturuluyor.

print("Çözülen Metin:",newText)
"""
