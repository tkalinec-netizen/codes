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


from Body import *
from Results import *
from Menu import *


class Allpack(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,relief=FLAT,background='red')
        
        Body(parent).pack(side=TOP, anchor=W, padx=5, pady=5)



def main():
    root=Tk()
    root.option_add('*Font', 'serif 9')
    root.title("Fourier")
    root.minsize(width=700,height=500)
    t=Toolbar(root)
    t.pack(side=TOP, fill=X)
    b=ButtonList(root)
    b.pack(side=BOTTOM, fill=BOTH)
    path = 'C:/obr/fig_1.gif'
    img = PhotoImage(file=path)
    panel = Label(root, image = img)
    
    panel.pack(side = RIGHT, anchor=W)
    Allpack(root).pack(side=LEFT)
    

    root.mainloop()

if __name__ == '__main__':
    main()

##root = Tk()
##
##mainloop()
