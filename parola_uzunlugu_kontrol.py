  

while True:
    parola=input("parola giriniz :") #şifre girişi istenir
    if len(parola)>8 and 14>len(parola):          #girilen şifre en az 8 en fazla 14 karakterli olması sart ile kontol edilir
    
        print("Aktif edilmiştir")     
        break                                   #şartlar saglanır ise Aktif edilmiştir yazar 
    else:
        print("parola en az 8 karakter olamlıdır en fazla 14 karakterli olmalıdır") # şart saglanmaz ise tekrar girilmesini ister 
      