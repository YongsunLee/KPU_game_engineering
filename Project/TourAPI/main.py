# -*- coding : UTF-8 -*-
from tkinter import *

class MyFrame(Frame):
    def __init__(self, master):
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        txt = Listbox(master, yscrollcommand=scrollbar.set)
        txt.insert(1, "서울")
        txt.insert(2, "인천")
        txt.insert(3, "인천")
        txt.insert(4, "인천")
        txt.insert(5, "인천")
        txt.insert(6, "인천")
        txt.insert(7, "인천")
        txt.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=txt.yview)

def main():
    root = Tk()
    root.title("TourAPI")
    root.geometry("320x80+100+100")
    myframe = MyFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
