kulaniciadi="çarşamba"
parola="myo"
                              #kulanıcı adı ve şifre belirlenmiştir 
while True:                   #şart doğru olana kadar while döngüsü devam eder
    a=input("Kulanıcı adı giriniz: ")          
    b=input("Parola giriniz: ")            # a ve b degişkenlerine karşılaştırma yapmak için kullanıcı adı ve şifre istenir
    if a==kulaniciadi and b==parola:       # kulanıcı adı ve şifre karşılaştırılır doğru ise while döngüsü kırılır giriş başarılı yazar
        print("Giriş başarılı")
        break
    else:
        print("yanlış deger girdiniz tekrar deneyiniz")   # şart saglanmaz iste işlem tekrar eder ne zaman doğru olursa ozaman döngü kırılır 