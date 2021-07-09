from tkinter import *

window = Tk()

def km_to_mile():
    print(e1_value.get())
    miles = float(e1_value.get()) * 0.621371
    t1.insert(END, miles)

b1 = Button(window, text='convert km to mile', comman=km_to_mile)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, width=20)
t1.grid(row=0, column=2)

window.mainloop()
