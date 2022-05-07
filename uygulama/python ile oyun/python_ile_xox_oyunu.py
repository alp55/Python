#python dilince 3x3 boyutunda tac toe (sos) oyununu geliştirelim bu oyun için 
# 1 dokuz adet button gerekli 2 bir oyuncunun oyunu kazanabilmesi için 8 ihtimal var (3 satır 3 stun 2 köşegen) 
# 3 oyuna başlarken bir oyuncu ataması yapmaylıyız örnegin birinci oyuncu x ikinci oyuncu y olsun 
from tkinter import*
from tkinter import messagebox
from turtle import bgcolor

root=Tk()
root.title="XOX OYUNU"


def XOX(buttons):
    global b_click
    
    if buttons["text"]==" " and b_click==True:
        buttons["text"]="X"
        buttons["bg"]="red"
        b_click=False 
       
    elif buttons["text"]==" " and b_click==False:
        buttons["text"]="O"
        buttons["bg"]="green"
        
        b_click=True
    
    if (
        (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X")or
        (button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X")or
        (button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X")or

        (button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X")or
        (button7["text"]=="X" and button5["text"]=="X" and button3["text"]=="X")or

        (button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X")or
        (button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X")or
        (button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X")):
        
        messagebox.showinfo("Kazandınız","X oyuncusu oyunu kazandı")
        soru=messagebox.askquestion("soru","tekrar oynamak ister misin ?")
        if soru=="yes":
            button1["text"]=" " 
            button1["bg"]="white"
            button2["text"]=" "
            button2["bg"]="white"
            button3["text"]=" "
            button3["bg"]="white"
            button4["text"]=" "
            button4["bg"]="white"
            button5["text"]=" "
            button5["bg"]="white"
            button6["text"]=" "
            button6["bg"]="white"
            button7["text"]=" "
            button7["bg"]="white"
            button8["text"]=" "
            button8["bg"]="white"
            button9["text"]=" "
            button9["bg"]="white"
            cevap=messagebox.askquestion("soru","Oyuna birinci oyuncu mu başlasın")
            if cevap=="yes":
                b_click=True

            else:
                b_click=False
        elif soru=="no":
            root.destroy()

        
        
    
    elif (
        (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O")or
        (button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O")or
        (button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O")or

        (button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O")or
        (button7["text"]=="O" and button5["text"]=="O" and button3["text"]=="O")or

        (button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O")or
        (button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O")or
        (button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O")):
        soru=messagebox.showinfo("Kazandınız","O oyuncusu oyunu kazandı")
        
        soru=messagebox.askquestion("soru","tekrar oynamak ister misin ?")
        if soru=="yes":
            button1["text"]=" " 
            button1["bg"]="white"
            button2["text"]=" "
            button2["bg"]="white"
            button3["text"]=" "
            button3["bg"]="white"
            button4["text"]=" "
            button4["bg"]="white"
            button5["text"]=" "
            button5["bg"]="white"
            button6["text"]=" "
            button6["bg"]="white"
            button7["text"]=" "
            button7["bg"]="white"
            button8["text"]=" "
            button8["bg"]="white"
            button9["text"]=" "
            button9["bg"]="white"
            cevap=messagebox.askquestion("soru","Oyuna birinci oyuncu mu başlasın")
            if cevap=="yes":
                b_click=True
            else:
                b_click=False           
        elif soru=="no":
            root.destroy()

    elif ( (button1["text"]=="X"or button1["text"]=="O")and (button2["text"]=="X"or button2["text"]=="O")and(button3["text"]=="X"or button3["text"]=="O")and(button4["text"]=="X"or button4["text"]=="O")and(button5["text"]=="X"or button5["text"]=="O")and(button6["text"]=="X"or button6["text"]=="O")and(button7["text"]=="X"or button7["text"]=="O") and (button8["text"]=="X"or button8["text"]=="O") and (button9["text"]=="X"or button9["text"]=="O")):
        soru=messagebox.showinfo("Berabere","Kimse kazanamadı")
        soru=messagebox.askquestion("soru","tekrar oynamak ister misin ?")
        if soru=="yes":
            button1["text"]=" " 
            button1["bg"]="white"
            button2["text"]=" "
            button2["bg"]="white"
            button3["text"]=" "
            button3["bg"]="white"
            button4["text"]=" "
            button4["bg"]="white"
            button5["text"]=" "
            button5["bg"]="white"
            button6["text"]=" "
            button6["bg"]="white"
            button7["text"]=" "
            button7["bg"]="white"
            button8["text"]=" "
            button8["bg"]="white"
            button9["text"]=" "
            button9["bg"]="white"
            cevap=messagebox.askquestion("soru","Oyuna birinci oyuncu mu başlasın")
            if cevap=="yes":
                b_click=True
            else:
                b_click=False           
        elif soru=="no":
            root.destroy()
            
           
buttons=StringVar()
button1=Button(root,text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:XOX(button1))
button1.grid(row=1,column=1,sticky=S+N+E+W)
button2=Button(root,text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:XOX(button2))
button2.grid(row=1,column=2,sticky=S+N+E+W)
button3=Button(root,text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:XOX(button3))
button3.grid(row=1,column=3,sticky=S+N+E+W)
button4=Button(root,text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:XOX(button4))
button4.grid(row=2,column=1,sticky=S+N+E+W)
button5=Button(root,text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:XOX(button5))
button5.grid(row=2,column=2,sticky=S+N+E+W)
button6=Button(root,text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:XOX(button6))
button6.grid(row=2,column=3,sticky=S+N+E+W)
button7=Button(root,text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:XOX(button7))
button7.grid(row=3,column=1,sticky=S+N+E+W)
button8=Button(root,text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:XOX(button8))
button8.grid(row=3,column=2,sticky=S+N+E+W)
button9=Button(root,text=" ",font=('Arial 30 bold'),height=4,width=8,command=lambda:XOX(button9))
button9.grid(row=3,column=3,sticky=S+N+E+W)



cevap=messagebox.askquestion("soru","Oyuna birinci oyuncu mu başlasın")

if cevap=="yes":
    b_click=True

else:
    
    b_click=False

root.mainloop()



    
