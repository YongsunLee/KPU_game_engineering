from tkinter import *
window = Tk()

l1 = Label(window, text="달러")
l2 = Label(window, text="원")
l1.pack()
l2.pack()

e1 = Entry(window)
e2 = Entry(window)
e1.pack()
e2.pack()

b1 = Button(window, text="달러->원")
b2 = Button(window, text="원->달러")
b1.pack()
b2.pack()

window.mainloop()