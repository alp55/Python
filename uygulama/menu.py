from tkinter import*
pencere=Tk()

def dosyakaydet():
    print("dosya kaydedildi")

def dosyaac():
    print("dosya açıldı")

def gerial():
    print("işlem geri alındı")

def ekle():
    print("Resim eklendi")

def yukle():
    print("PDF yüklendi")

menu=Menu(pencere)
subMenu=Menu(menu)
pencere.config(menu=menu)
menu.add_cascade(label="Dosya",menu=subMenu)
subMenu.add_command(label="Kaydet", command=dosyakaydet)
subMenu.add_command(label="Aç",command=dosyaac)
subMenu.add_separator()
subMenu.add_command(label="Çıkış",command=pencere.destroy)

editMenu=Menu(menu)
menu.add_cascade(label="Düzenle",menu=editMenu)
editMenu.add_command(label="Geri al",command=gerial)

araccubugu=Frame(pencere,bg="red")
resimekle=Button(araccubugu,text="Resim Ekle",command=ekle)
resimekle.pack(side=LEFT,padx=2,pady=2)
pdfyukle=Button(araccubugu,text="PDF Yukle",command=yukle)
pdfyukle.pack(side=LEFT,padx=2,pady=2)
araccubugu.pack(side=TOP,fill=X)

durumcubugu=Label(pencere,text="Sayfa yükleniyor...",bd=3,relief=SUNKEN,
                  anchor=W)
durumcubugu.pack(side=BOTTOM,fill=X)
                

pencere.mainloop()
