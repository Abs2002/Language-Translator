from tkinter import *
from tkinter.ttk import *
from googletrans import Translator
from tkinter import messagebox

try:
    rt=Tk()
    rt.geometry("600x200")
    rt.title("Language Translator 1.0.1")


    sc1=StringVar()
    sc2=StringVar()

    language_pack={"English":"en", "Hindi":"hi", "Tamil":"ta", "Telegu":"tu","Chinese (Simplified)":"zh-CN", "French":"fr", "German":"de", "Italian":"it", "Japanese":"ja", "Korean":"ko",
                   "Norwegian":"no", "Portugese":"pt", "Russian":"ru", "Spanish":"es"}



    e1=Entry(rt, font=(22), textvariable=sc1)
    e2=Entry(rt, font=(22), textvariable=sc2)
    e1.place(x=30, y=30)
    e2.place(x=30, y=90)

    cm1=Combobox(rt, font=(22), width=10)
    cm1['values']=tuple(language_pack.keys())
    cm1.current(0)
    cm1.place(x=370, y=30)

    cm2=Combobox(rt, font=(22), width=10)
    cm2['values']=tuple(language_pack.keys())
    cm2.current(0)
    cm2.place(x=370, y=90)

    def wtrans():
        a=sc1.get()
        b=sc2.get()
        translator=Translator()
        if cm1.get()==cm2.get():
            messagebox.showinfo("Hey", "Are you Nuts")
        else:
            if a!="" and b=="":
                c = translator.translate(a, dest=f"{language_pack.get(cm2.get())}")
                sc2.set(c.text)
            elif a=="" and b!="":
                c = translator.translate(b, dest=f"{language_pack.get(cm1.get())}")
                sc1.set(c.text)



    b1=Button(rt, text="Translate", command=wtrans)
    b1.place(x=360, y=150)

    def clear():
        sc1.set("")
        sc2.set("")

    b2=Button(rt, text="Clear All", command=clear)
    b2.place(x=100, y=150)

    def c1():
        sc1.set("")

    def c2():
        sc2.set("")

    b3=Button(rt, text="<-", command=c1)
    b3.place(x=270, y=30)

    b4=Button(rt, text="<-", command=c2)
    b4.place(x=270, y=90)

    rt.mainloop()

except:
    messagebox.showinfo("Oops!", "Looks like You are not connected to network\nor you network is slow Try Again")

