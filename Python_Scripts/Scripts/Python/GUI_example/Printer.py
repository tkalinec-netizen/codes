#-------------------------------------------------------------------------------
# Name:        modulPrinter
# Purpose:
#
# Author:      Tomáš
#
# Created:     20.03.2014
# Copyright:   (c) Tomáš 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
import tkinter.colorchooser
from tkinter.messagebox import *
import tkinter.filedialog
from PIL import Image, ImageTk

def Pr():
        askokcancel('Print','I´m printing')

def main():

    def Print():
        askokcancel('Print','I´m printing')
    root=Tk()
    root.title("Print")
    root.geometry("400x300+100+100")
    root.resizable(width=NO, height=NO)
    txts=['Name:', 'State:', 'Type:', 'Location:']
    bts=['All','Sites', 'Choose']
    choice=StringVar()
    choice.set('All')

    root.option_add('*Font', 'serif 9')
    lf1=LabelFrame(root,text="Printer")
    s1=StringVar()
    s1.set('0')
    s2=StringVar()
    s2.set('0')
    lf2=LabelFrame(root,text='Print area')
    lf3=LabelFrame(root, text='Copy')
    f1=Frame(lf1)
    f2=Frame(lf2)
    f5=Frame(lf2)
    f4=Frame(root)
    f3=Frame(root)
    f7=Frame(lf3)
    f8=Frame(lf1)
    f9=Frame(root)

    for label in txts:
        Label(f1, text=label).pack(side=TOP,pady=5, padx=3, anchor=W)


    for button in bts:
        r=Radiobutton(f5, text=button,variable=choice, value=button)
        r.pack(side=TOP, anchor=W, padx=3)
    r.config(state=DISABLED)
    param=['Hp deskjet 920c', 'Microsoft Document Writer', 'eDoc Printer']
    pr=StringVar(root)
    pr.set(param[0])

    def Text(value):

        if pr.get()==param[0]:
            l1.config(text='Ready')
            l2.config(text='Hp deskjet 920c')
            l3.config(text='USB001')

        elif pr.get()==param[1]:
            l1.config(text='Ready')
            l2.config(text='Microsoft XPS writer')
            l3.config(text='XPSPort')

        elif pr.get()==param[2]:
            l1.config(text='Ready')
            l2.config(text='eDoc Printer')
            l3.config(text='USBx54')

    o=OptionMenu(f8,pr,*param, command=Text)
    o.pack()
    o.config(width=20, anchor=W, relief=RIDGE)
    l1=Label(f8, text='Ready')
    l2=Label(f8, text='Hp deskjet 920c')
    l3=Label(f8, text = 'USB001')
    l1.pack(side=TOP, anchor=W, pady=5)
    l2.pack(side=TOP, anchor=W, pady=5)
    l3.pack(side=TOP, anchor=W, pady=5)

    Button(lf1, text='Properties',width=12).pack(side=RIGHT, anchor=N,pady=2, padx=5)

    Label(f2,text='from:').pack(side=LEFT)
    Entry(f2, textvariable=s1, width=3).pack(side=LEFT)
    Label(f2,text='to:').pack(side=LEFT)
    Entry(f2, textvariable=s2, width=3).pack(side=LEFT)

    Label(f7, text='Number of copies:').pack(side=LEFT, anchor=N)
    Spinbox(f7,width=3, values=(range(1,50))).pack(side=LEFT, anchor=N, padx=5)
    photo = PhotoImage(file='C:/obr/pr.gif')
    label = Label(lf3,image=photo)
    label.pack(side=BOTTOM)

    Button(f9,text='Storno', command=root.destroy).pack(side=RIGHT, padx=5)
    Button(f9,text='OK', command=Pr).pack(side=RIGHT, padx=5)

    f5.pack(side=LEFT, anchor=W)
    f2.pack(side=LEFT)
    f1.pack(side=LEFT, anchor=N)
    f7.pack(side=LEFT, anchor=N)
    f8.pack(side=LEFT, anchor=N)
    f9.pack(side=BOTTOM, anchor=SE)
    lf1.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand="yes" )
    lf2.pack(side=LEFT, padx=5, pady=5,fill=BOTH, expand="yes")
    lf3.pack(side=RIGHT, padx=5, pady=5, fill=BOTH, expand="yes")


    mainloop()


if __name__ == '__main__':
    main()

