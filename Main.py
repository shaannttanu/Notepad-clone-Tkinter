from tkinter import *
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def New():
    global file
    textarea.delete(1.0,END)
    file=None
    root.title('Untitled Notepad')
    textarea.update()

def Open():
    global file
    file=askopenfilename(defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Files','*.txt')])
    with open(file) as f:
        textarea.insert(1.0,f.read())
        name=os.path.basename(file)
        root.title(os.path.splitext(name)[0] + ' - Notepad')

def Save():
    global file
    file=asksaveasfilename(defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Files','*.txt')]
                           ,initialfile='Untitled')
    with open(file,'w') as f:
        f.write(textarea.get(1.0,END))
        name = os.path.basename(file)
        root.title(os.path.splitext(name)[0] + ' - Notepad')

def Cut():
    textarea.event_generate('<<Cut>>')

def Copy():
    textarea.event_generate('<<Copy>>')

def Paste():
    textarea.event_generate('<<Paste>>')

def Help():
    msg.showinfo('About','Developed By Shantanu Singh under Trux lab Co. Ltd.')

if __name__ == '__main__':

    file=None
    root=Tk()
    root.geometry('432x211')
    root.title('Untitled Notepad')
    textarea=Text(root,font='lucida 12')
    textarea.pack(fill=BOTH,expand=TRUE)

    menubar=Menu(root)
    fileMenu=Menu(menubar,tearoff=0)
    fileMenu.add_command(label="New",command=New)
    fileMenu.add_command(label="Open",command=Open)
    fileMenu.add_command(label="Save",command=Save)
    fileMenu.add_command(label="Quit",command=quit)
    menubar.add_cascade(label="File",menu=fileMenu)

    editMenu=Menu(menubar,tearoff=0)
    editMenu.add_command(label='Cut',command=Cut)
    editMenu.add_command(label='Copy',command=Copy)
    editMenu.add_command(label='Paste',command=Paste)
    menubar.add_cascade(label='Edit',menu=editMenu)

    helpMenu=Menu(menubar,tearoff=0)
    helpMenu.add_command(label='About',command=Help)
    menubar.add_cascade(label='Help',menu=helpMenu)
    root.config(menu=menubar)
    root.mainloop()
