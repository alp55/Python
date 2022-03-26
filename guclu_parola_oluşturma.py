import string
buyukharf=string.ascii_uppercase+"ĞÇŞÜÖİ"  #parametrenin içinde olmadıgı için türkçe büyük karakterleri ekledik
kucukharf=string.ascii_lowercase+"ğçşüöı"  #parametrenin içinde olmadıgı için türkçe kücük karakterleri ekledik
rakamlar=string.digits
ozelkar=string.punctuation

#Güclü bir parola oluşturabilmek için En Az birer tane büyük harf kücük harf numara ve özel karakter olmalıdır
#bu şartları sağlayabilmek için degişkenlere tüm harfleri sayıları ve özel karakterleri atadık

kucukharf_var=False
buyukharf_var=False
rakamlar_var=False
ozelkar_var=False

#degerler kontrol etmek için false yapılır

while  True: #şart doğru ise döngüden çık
    parola=input("sifre gir ") #şifre girişi istenir
    for i in parola :         #girilen parola i degişkeni ile döngüye sokulur ve i degişkenine yazdırılır
    
        if i in kucukharf :               
            kucukharf_var=True
    
        if i in buyukharf :
            buyukharf_var=True
                   #i degişkeni ile büyük harf kücük harf numara ve özel karakterler karşılaştırlır içerisinde geciyorsa True degeri alır
        if i in rakamlar:
            rakamlar_var=True
    
        if i in ozelkar:
            ozelkar_var=True  

    if len(parola)>8 and 14>len(parola) and kucukharf_var and buyukharf_var and ozelkar_var and rakamlar_var==1:
        #if ile istelilen şartları saglayıp saglmadıgı kontol edilir şart saglanıyorsa while döngüsü kırılır program kapanır
        print("parola gecerli bir paroladır") 
        break
    else :
        print("parola geçerli degildir tekarar deneyiniz")
   

    

