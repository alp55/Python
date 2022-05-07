from tkinter import*
from tkinter import messagebox

pencere=Tk()

cevap=messagebox.askquestion("Soru","Devam etmek istiyor musunuz")
if cevap=="yes":
    print("giriş")
else :
    print("cıkış")

pencere.mainloop()
    
