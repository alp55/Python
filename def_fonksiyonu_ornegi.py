# programın amacı def kulanarak cift ve tek sayilari 
# def fonksiyonuna gönderek toplatmak

liste=[]
cifttop=0
tekttop=0

def cift(ls,t): 
    t+=ls
    return t
              # cift ve tek için iki def belirledim
def tek(lk,tek):
    tek+=lk
    return tek

girileceksayiadedi=int(input("Kaç adet sayi gireceksiniz")) # kac adet sayi girilecegi istenir

for sayi in range(girileceksayiadedi): # girilen sayı kadar göndü 1 den başalayarak döner 
    
    liste.append(int(input("{}. sayiyi giriniz".format(sayi+1)))) # istenilen sayi kadar liste fonksiyonuna deger girdirilir
    
    if liste[sayi]%2==0: # eger sayi 2 ye kalansız bölünüyorsa
        cifttop=cift(liste[sayi],cifttop)  # cifttop degişkeni def cift() fonkisiyonun degerini alsın
    else:  # şart saglanmaz ise
        tekttop=tek(liste[sayi],tekttop)  # tektop degişkeni de tek() fonkisiyonun degerini alsın

print("tek sayiların toplamı: {}".format(tekttop))  
                                                    # cifttop ve tektop ekrana yazdırılır  
print("cift sayiların toplamı: {}".format(cifttop))