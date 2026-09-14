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
from Results import *

class Info(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.p=parent
        self.str=StringVar()
        Label(self, text='Information:', underline=True).pack(side=TOP, anchor=W, padx=3, pady=3)
        Label(self, text='Function:').pack(side=LEFT, anchor=W, padx=3, pady=3)
        e=Entry(self, width=15, textvariable=self.str)
        e.pack(side=LEFT, padx=3, pady=3)
        self.res=e.get()
        e.focus_set()
        b=Button(self, text='OK', command=self.read)
        b.pack(side=LEFT)

    def read(self):
        print (self.str.get())


class Range(Frame):
    def __init__(self, parent, label, labelwidth=12):
        Frame.__init__(self,parent)
        self.p=parent
        Label(self, text=label, width=labelwidth).pack(side=LEFT, padx=3,
        pady=3, anchor=E)
        self.var1=DoubleVar(value=0)
        self.var2=DoubleVar(value=0)
        Entry(self, width=5, textvariable=self.var1).pack(side=LEFT, padx=3, pady=3)
        Entry(self, width=5, textvariable=self.var2).pack(side=LEFT, padx=3, pady=3)


class Plots(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
##        Label(text='contours')
        self.p=parent
        l=LabelFrame(self, text='Plots')
        l.pack(side=TOP)
        plot1=['Line', 'Contour', 'Vector']
        plot2 = ['Scatter', 'Rose', 'Polar']
        f1=Frame(l)
        f2=Frame(l)
        for plot in plot1:
            Checkbutton(f1, text=plot).pack(side=LEFT, padx=3, pady=3, anchor=W)
        for plot in plot2:
            Checkbutton(f2, text=plot).pack(side=LEFT, padx=3, pady=3, anchor=W)

        f1.pack(side=TOP, anchor=W)
        f2.pack(side=TOP, anchor=W)



class ButtonList(Frame):
    def __init__(self, parent, *k):
        Frame.__init__(self,parent, relief=RAISED, borderwidth=1)
        self.p=parent
        self.k=k
        print (self.k)
        self.initUI()
##        self.b=Body(parent)
##        self.b.pack(side=TOP, anchor=W, padx=5, pady=5)


    def initUI(self):
        self.b1=Button(self, text='Plot', width=9, bd=2)
        self.b2=Button(self, text='Clear',  width=9, bd=2)
        self.b3=Button(self, text='Import>>', width=9, bd=2, command=self.Res)
        self.b1.pack(fill=X, side=LEFT, padx=10, pady=5, anchor=W)
        self.b2.pack(fill=X, side=LEFT, padx=10, pady=5, anchor=W)
        self.b3.pack(fill=X, side=RIGHT, anchor=E, padx=10, pady=5)


    def Res(self):
        self.r=Result(self.p)
        self.r.pack()
        self.b3.config(state=DISABLED)   


class Boundary(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.p=parent
        self.var=IntVar(value=0)
        lf=LabelFrame(self, text='Boundary conditions')
        lf.pack(padx=1, pady=5, anchor=W)
        Radiobutton(lf,text='Dirichlet on both sides', value=0, variable=self.
        var).pack(padx=3, pady=3, anchor=W)
        Radiobutton(lf,text='Neumann on both sides', value=1, variable=self.
        var).pack(padx=3, pady=3, anchor=W)
        Radiobutton(lf,text='Dirichlet on the left, neumann on the right',
        value=2, variable=self.var).pack(padx=3, pady=3)



class Body(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent,relief=GROOVE, bd=2)
        self.p=parent
        Boundary(self).pack(side=TOP, anchor=W)
        Plots(self).pack(side=TOP, anchor=W)
        lf=LabelFrame(self,text='Data' ,relief=SUNKEN, bd=1)
        f=Frame(lf, borderwidth=1)
        Label(f, text='Coordinate:').pack(side=LEFT, anchor=W, padx=3, pady=3)
        Label(f, text='  X', width=9).pack(side=LEFT, padx=3, pady=3)
        Label(f, text='Y', width=2).pack(side=LEFT, padx=3, pady=3)
        f.pack(side=TOP, anchor=W)
        Range(lf, 'Axes:').pack(side=TOP, anchor=W)
        Range(lf, 'XRange:').pack(side=TOP, anchor=W)
        Range(lf, 'XRange:').pack(side=TOP, anchor=W)
        i=Info(self)
        i.pack(side=BOTTOM, anchor=W)
        self.res=i.str.get()
        print ('Function is: '+i.str.get())

        lf.pack(side=TOP, anchor=W)


def main():
    root=Tk()
    root.option_add('*Font', 'serif 9')
    root.title("Fourier")
    root.minsize(width=700,height=500)
    path = 'C:/obr/fig_1.gif'
    img = PhotoImage(file=path)
    panel = Label(root, image = img)
    panel.pack(side = RIGHT)
    bl=ButtonList(root)
    bl.pack(side=BOTTOM, fill=BOTH)
    b=Body(root)
    b.pack(side=TOP, anchor=W, padx=5, pady=5)
    mainloop()

if __name__ == '__main__':
    main()
