#kulanıcı adı girilerek bir sisteme dahil olunmak istenmektedir 
# kullanıcı adı doğrulanmak için kişiye 3 hak verilmiştir 
#doğru ad girildiginde sisteme giriş yapan yanlış cevap girildiginde kulanıcıya
#kac hakkı kaldıgını belirterek kulanıcını hakkı kalmadıgında ise sitemi kapatan 
# programı while döngüsü ile yapınız bu soruyu if yapıları ile cözünüz 


cevap="alperen" #kulanıcı adımız alperen olsun istedim :)

hak=3# sorumuzda verildigi gibi 3 hakımız olacak

while hak>=1: # while döngü bir haktan az kaldıgında kırılır

    kulaniciadi=input("kulanici adi giriniz:") # kulanıcı adi girilmesini istiyoruz

    hak=hak-1 # kulanıci adi girildikce hak azalır

    if kulaniciadi==cevap: # cevap ile kullaniciadi karşılaştırılır aynı ise giriş başarılı yazar break komutu ile while dönügüsü kırlır
        print("giriş başarılı")
        break
    if hak>0:  # hak hala varsa
        
        print("hakınız kaldı {} giriş başarısız ".format(hak))  # kaç hak kaldıgını kulanıcıya geri bildiri yapar
    else:
        print ("hiç hakınız kalmadı") # hak bitmiştir
    