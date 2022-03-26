a=int(input("bir sayı giriniz: "))          
b=int(input("ikinci sayıyı giriniz: "))
                                         # iki tane degişkene sayı girişi istenir
print("toplama için 1 çıkartma 2 çarpma 3 bölme 4 e basınız")
                                              # yapılmak istenen 4 işlem için sayı atanır girilen sayı if else metodu ile karşılaştırılır
islem=int(input("yapmak istediginiz işlemi giriniz: "))

if islem==1:            
    print(a+b)           
elif islem==2:
    print(a-b)
elif islem==3:
    print(a*b)
elif islem==4:
    print(a/b)             # girilen sayıya  karşılık gelen dört işleden birini yapar ve erkana yazdırır
else :
   print("yanlış işlem yaptınız")