#-------------------------------------------------------------------------------
# Name:        modul1
# Purpose:
#
# Author:      Tomáš
#
# Created:     19.03.2014
# Copyright:   (c) Tomáš 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.colorchooser
from tkinter.messagebox import *
import tkinter.filedialog
from PIL import Image, ImageTk

class MenuBar(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()


    def initUI(self):
##        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="New ...", command=self.New)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label = 'Save', command = self.SaveFile)
        imp = Menu(fileMenu, tearoff=0)
        imp.add_command(label="New feed")
        imp.add_command(label="Bookmarks")
        imp.add_command(label="Mail")
        fileMenu.add_cascade(label='Import', menu=imp)
        fileMenu.add_cascade(label='Close', command=self.callback)
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=self.parent.destroy)

        edit=Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Edit', menu=edit)
        ##m2.add_command()
        edit.add_cascade(label='Back')
        edit.add_cascade(label='Cut')
        edit.add_cascade(label='Copy')
        edit.add_separator()
        edit.add_cascade(label='Format')


        view=Menu(menubar, tearoff=0)
        menubar.add_cascade(label='View', menu=view)

        self.var1=IntVar(value=1)
        self.var2=IntVar()

        view.add_cascade(label='Back')
        view.add_cascade(label='Cut')
        view.add_cascade(label='Copy')
        view.add_separator()
        submenu = Menu(view, tearoff=0)
        submenu.add_checkbutton(label="English", variable=self.var1)
        submenu.add_checkbutton(label="Czech", variable=self.var2.set(0))
        submenu.add_checkbutton(label="French", variable=self.var2.set(0))
        submenu.add_checkbutton(label="German", variable=self.var2.set(0))
        view.add_cascade(label="Language", menu=submenu, underline=0)

        view.add_separator()
        view.add_cascade(label='Enlarge')
        view.add_cascade(label='Reduce')

        tools=Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Tools', menu=tools)
        tools.add_cascade(label='Options')
        tools.add_command(label='Color', command=self.onChoose)
        tools.add_command(label='Print', command=self.Print)
        tools.add_separator()
        tools.add_cascade(label='Network manager')

        info = Menu(menubar, tearoff=0)
        info.add_command(label="Support", command=self.app)
        menubar.add_cascade(label="Help", menu=info)
        info.add_command(label = 'About...', command=self.Info)

    def NewFile(self):
        print ("New file")

    def onChoose(self):
        (rgb, hx) = tkinter.colorchooser.askcolor()


    def app(self):
        t=Toplevel(self.parent)
        t.title("Info")
        t.geometry("300x100+100+100")
        Label(t, text='This is real time version. \n It is prohibited to copy and use this for another\n purpose than '
        'it is determited.\n Created by Tomas Kalinec').pack(side=TOP)
        t.resizable(width=NO, height=NO)
        t.mainloop()


    def SaveFile(self):
        ftypes = [('Python files', '*.py'), ('All files', '*')]
        name = tkinter.filedialog.asksaveasfile(title='Save file',initialdir='C:', filetypes=ftypes)
        print (name)

    def Info(self):
        showinfo("About", "Version 1.1")
        
    def newWindow(self):
        t=Toplevel(self.parent)
        t.title('File')
        self.TMenu(t)
        txt = Text(t)
        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = tkinter.filedialog.Open(self, filetypes = ftypes)
        

    def onOpen(self):

        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = tkinter.filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

    def TMenu(self, t):
        menubar = Menu(t)
        t.config(menu=menubar)
        fileMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label = 'Save', command =  self.SaveTxt)
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=self.parent.destroy)

    def SaveTxt(self):
        ftypes = [('ext files', '*.txt'), ('All files', '*')]
        name = tkinter.filedialog.asksaveasfile(title='Save file as',initialdir='C:', filetypes=ftypes)

    def readFile(self, filename):

        f = open(filename, "r")
        text = f.read()
        return text

    def callback(self):
        if askyesno('Verify', 'Really quit?'):
            self.parent.destroy()
        else:
            showinfo('No', 'Quit has been cancelled')

    def New(self):
        t=Toplevel(self.parent)
        t.title('New')
        t.geometry("350x200+100+100")
        t.resizable(width=NO, height=NO)

        f1=Frame(t)
        Label(f1, text='New', underline=1).pack(side=TOP, padx=5, pady=5, anchor=W)
        l = Listbox(f1, width=30, height=5)
        items=['Python script', 'Bitmap', 'New picture', 'XML Document']
        for item in items:
            l.insert(END, item)
        l.pack(padx=5, pady=5)
        f1.pack(side=LEFT, fill=BOTH)

        f2=Frame(t)

        Button(f2,text='OK', width=7, command=self.newWindow).pack(side=TOP, anchor=W, padx=5, pady=5)
        Button(f2, text='Cancel', width=7, command=t.destroy).pack(side=TOP, anchor=W, padx=5, pady=5)
        f2.pack(side=RIGHT, fill=BOTH)

    def Text(self, value):
        print (self.pr.set(value))
        print (self.pr.get())

        if self.pr.get()==self.param[0]:
            self.l1.config(text='Ready')
            self.l2.config(text='Hp deskjet 920c')
            self.l3.config(text='USB001')

        elif self.pr.get()==self.param[1]:
            self.l1.config(text='Ready')
            self.l2.config(text='Microsoft XPS writer')
            self.l3.config(text='XPSPort')

        elif self.pr.get()==self.param[2]:
            self.l1.config(text='Ready')
            self.l2.config(text='eDoc Printer')
            self.l3.config(text='USBx54')


    def Print(self):
        self.t=Toplevel(self.parent)
        self.t.geometry("400x300+100+100")
        self.t.title("Print")
        self.t.resizable(width=NO, height=NO)
        txts=['Name:', 'State:', 'Type:', 'Location:']
        bts=['All','Sites', 'Choose']
        choice=StringVar(self.t)
        choice.set('All')
        self.t.option_add('*Font', 'serif 9')
        lf1=LabelFrame(self.t,text="Printer")
        s1=StringVar()
        s1.set('0')
        s2=StringVar()
        s2.set('0')
        lf2=LabelFrame(self.t,text='Print area')
        lf3=LabelFrame(self.t, text='Copy')
        f1=Frame(lf1)
        f2=Frame(lf2)
        f5=Frame(lf2)
        f4=Frame(self.t)
        f3=Frame(self.t)
        f7=Frame(lf3)
        f8=Frame(lf1)
        f9=Frame(self.t)

        for label in txts:
            Label(f1, text=label).pack(side=TOP,pady=5, padx=3, anchor=W)

        for button in bts:
            r=Radiobutton(f5, text=button,variable=choice, value=button)
            r.pack(side=TOP, anchor=W, padx=3)
        r.config(state=DISABLED)
        self.param=['Hp deskjet 920c', 'Microsoft Document Writer', 'eDoc Printer']
        self.pr=StringVar(self.t)
        self.pr.set(self.param[0])

        o=OptionMenu(f8,self.pr,*self.param, command=self.Text)
        o.pack()
        o.config(width=20, anchor=W, relief=RIDGE)
        self.l1=Label(f8, text='Ready')
        self.l2=Label(f8, text='Hp deskjet 920c')
        self.l3=Label(f8, text = 'USB001')
        self.l1.pack(side=TOP, anchor=W, pady=5)
        self.l2.pack(side=TOP, anchor=W, pady=5)
        self.l3.pack(side=TOP, anchor=W, pady=5)

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

        Button(f9,text='Storno', command=self.t.destroy).pack(side=RIGHT, padx=5)
        Button(f9,text='OK', command=self.Pr).pack(side=RIGHT, padx=5)

        f5.pack(side=LEFT, anchor=W)
        f2.pack(side=LEFT)
        f1.pack(side=LEFT, anchor=N)
        f7.pack(side=LEFT, anchor=N)
        f8.pack(side=LEFT, anchor=N)
        f9.pack(side=BOTTOM, anchor=SE)
        lf1.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand="yes" )
        lf2.pack(side=LEFT, padx=5, pady=5,fill=BOTH, expand="yes")
        lf3.pack(side=RIGHT, padx=5, pady=5, fill=BOTH, expand="yes")
        self.t.mainloop()

    def Pr(self):
        askokcancel('Print','I´m printing')
        self.t.destroy()



class Toolbar(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, relief=SUNKEN)
        self.m=MenuBar(parent)

        self.p=parent
        self.initUI()

    def initUI(self):
        f=Frame(self.p, bd=1, relief=RAISED)

        f.pack(side=TOP, fill=X)
        path = 'C:\obr\system.gif'
        img1 = PhotoImage(file=path)
        img2=PhotoImage(file='C:/obr/doc.gif')
        img3=PhotoImage(file='C:/obr/pis.gif')
        img4=PhotoImage(file='C:/obr/tisk.gif')
        img5=PhotoImage(file='C:/obr/save.gif')
        img6=PhotoImage(file='C:/obr/exit.gif')
        img7=PhotoImage(file='C:/obr/ar.gif')
        img7=PhotoImage(file='C:/obr/minus.gif')
        img8=PhotoImage(file='C:/obr/plus.gif')
        img9=PhotoImage(file='C:/obr/cut.gif')

        panel1 = Button(f, image = img2, fg='green', width=30, heigh=30, command=self.m.onOpen)
        panel2= Button(f, image = img9, fg='green', width=30, heigh=30)
        panel3= Button(f, image = img5, fg='green', width=30, heigh=30, command=self.m.SaveFile)
        panel4= Button(f, image = img1, fg='green', width=30, heigh=30)
        panel5= Button(f, image = img3, fg='green', width=30, heigh=30)
        panel6= Button(f, image = img4, fg='green', width=30, heigh=30, command=self.m.Print)
        panel7= Button(f, image = img7, fg='green', width=30, heigh=30)
        panel8= Button(f, image = img8, fg='green', width=30, heigh=30)
        panel9= Button(f, image = img6, fg='green', width=30, heigh=30, command=self.callback)

        panel1.image=img2
        panel2.image=img9
        panel3.image=img5
        panel4.image=img1
        panel5.image=img3
        panel6.image=img4
        panel7.image=img7
        panel8.image=img8
        panel9.image=img6

        panel1.pack(side = "left", fill = "both", expand = "no")
        panel2.pack(side = "left", fill = "both", expand = "no")
        panel3.pack(side = "left", fill = "both", expand = "no")
        panel4.pack(side = "left", fill = "both", expand = "no")
        panel5.pack(side = "left", fill = "both", expand = "no")
        panel6.pack(side = "left", fill = "both", expand = "no")
        panel7.pack(side = "left", fill = "both", expand = "no")
        panel8.pack(side = "left", fill = "both", expand = "no")
        panel9.pack(side = "left", fill = "both", expand = "no")

    def answer(self):
        showerror("Answer", "Sorry, no answer available")

    def callback(self):
        if askyesno('Verify', 'Really quit?'):
            self.p.destroy()
        else:
            showinfo('No', 'Quit has been cancelled')



def main():

    root = Tk()
    root.option_add('*Font', 'serif 9')
    root.title("Fourier")
    root.minsize(width=700,height=500)
##    ex = MenuBar(root)
##    ex.pack()
    t=Toolbar(root)
    t.pack(side=TOP, fill=X)
    root.geometry("700x500+100+100")
    root.mainloop()


if __name__ == '__main__':
    main()

