from tkinter import *

def calbuttonclick(event):
    global calstval
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        if calstval.get().isdigit():
            value=int(calstval.get())
        else:
            value=eval(calscre.get()) 
        calstval.set(value)
        calscre.update()
    elif text == "C":
        calstval.set("")
        calscre.update()
    else:
        calstval.set(calstval.get() + text)
        calscre.update()


edufabrica_calculator=Tk()
edufabrica_calculator.geometry("360x1080")
edufabrica_calculator.title("Edufabrica_Calculator")

calstval= StringVar()
calstval.set("")
calscre=Entry(edufabrica_calculator, textvar=calstval, font="poppin",)
calscre.pack(fill=X)
calframe=Frame(edufabrica_calculator)


calbutton=Button(calframe, text="/", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calbutton=Button(calframe, text="*", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calbutton=Button(calframe, text="C", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calframe.pack()

calframe=Frame(edufabrica_calculator)


calbutton=Button(calframe, text="=", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calbutton=Button(calframe, text="0", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calbutton=Button(calframe, text=".", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calframe.pack()
calframe=Frame(edufabrica_calculator)


calbutton=Button(calframe, text="+", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calbutton=Button(calframe, text="-", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calbutton=Button(calframe, text="%", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calframe.pack()

calframe=Frame(edufabrica_calculator)


calbutton=Button(calframe, text="7", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calbutton=Button(calframe, text="8", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calbutton=Button(calframe, text="9", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calframe.pack()

calframe=Frame(edufabrica_calculator)


calbutton=Button(calframe, text="4", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calbutton=Button(calframe, text="5", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calbutton=Button(calframe, text="6", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calframe.pack()

calframe=Frame(edufabrica_calculator)


calbutton=Button(calframe, text="1", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calbutton=Button(calframe, text="2", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calbutton=Button(calframe, text="3", font="poppin", padx=40,pady=40)
calbutton.pack(side=LEFT)
calbutton.bind("<Button-1>", calbuttonclick)
calframe.pack()






mainloop()