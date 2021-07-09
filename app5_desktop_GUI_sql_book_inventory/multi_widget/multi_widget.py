from tkinter import *

window = Tk()

def convert():
    print(e1_value.get())
    gram = float(e1_value.get()) * 1e3
    pound = float(e1_value.get()) * 2.20462
    ounce = float(e1_value.get()) * 35.274

    t1.delete("1.0", END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)

e0=Label(window,text="Input in [Kg]")
e0.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text='convert', comman=convert)
b1.grid(row=0, column=2)

e10=Label(window,text="[gram]")
e10.grid(row=1,column=0)

e11=Label(window,text="[pound]")
e11.grid(row=1,column=1)

e12=Label(window,text="[ounce]")
e12.grid(row=1,column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=2, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=2, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=2, column=2)
window.mainloop()
