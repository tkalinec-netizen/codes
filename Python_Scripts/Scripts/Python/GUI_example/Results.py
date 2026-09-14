#-------------------------------------------------------------------------------
# Name:        modul1
# Purpose:
#
# Author:      Tomáš
#
# Created:     22.03.2014
# Copyright:   (c) Tomáš 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from tkinter import *
from Menu import *
import tkinter.filedialog

class Result(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root=root
        self.root.resizable(width=False,height=True)
        self.UInit()

    def UInit(self):

        fr1 = Frame(self.root)
        fr1.pack(side=LEFT, anchor=N)
        lf=LabelFrame(fr1, text='Resulting:')
        lf.pack(pady=10, side=TOP, anchor=W)
        listbox = Listbox(lf)
        listbox.pack(side=LEFT, fill=Y, padx=5, pady=5)

        for item in "log(5)*x x^2+y^2 log(y)*exp(y)-sin(y) tg(x)-sin(y)".split():
            listbox.insert(END, item)

        fr2 = Frame(self, relief=FLAT, bd=2)
        self.b1=Button(fr2, text='Save as ..', width=8, command=self.SaveTxt)
        self.b1.pack(side=TOP, padx=5, pady=5, anchor=N)
        Button(fr2, text='Close', width=8, command=self.root.destroy).pack(side=BOTTOM,padx=5, pady=5, anchor=W)
        fr2.pack(side=RIGHT, fill=BOTH)
        items=listbox.get(0, END)
        self.t=Text()
        print (items)
        for item in items:
            self.t.insert(END, item+'\n')

    def SaveTxt(self):
        ftypes = [('Text files', '*.txt'), ('All files', '*')]
        name = tkinter.filedialog.asksaveasfile(title='Save file as',initialdir='C:',
         filetypes=ftypes, defaultextension=".txt")
        name.write(self.t.get(0.0,END))



def main():
    root=Tk()
    root.resizable(width=False, height=True)
    Result(root).pack()
    mainloop()

if __name__ == '__main__':
    main()
