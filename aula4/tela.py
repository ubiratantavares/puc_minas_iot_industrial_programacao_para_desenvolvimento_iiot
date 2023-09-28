# Gerar executável para windows

# pip install pyinstaller

# pyinstaller --onefile tela.py --noconsole

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import aula4.tela_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

class Toplevel1:

    def calcular(self):
        altura =   float(self.altura.get())
        raio = float(self.diametro.get())/2
        area = round(3.14*raio**2*altura)
        self.Label3_3.configure(text='Volume: '+str(area)+" m²")

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("1327x711+114+137")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#2e3349")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.altura = tk.StringVar()
        self.diametro = tk.StringVar()

        self.menubar = tk.Menu(top,font="TkMenuFont", bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.588, rely=-0.042, height=886, width=1167)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#2e3349")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        photo_location = os.path.join(_location,"aula3/imagens/tanque.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.039, rely=0.239, relheight=0.726
                , relwidth=0.529)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#252a40")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.148, rely=0.128, height=79, width=166)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#252a40")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 22")
        self.Label3.configure(foreground="#f2f2f2")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Altura [m]:''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.252, rely=0.734, height=74, width=307)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#007ef9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 28 -weight bold")
        self.Button1.configure(foreground="#f2f2f2")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Alterar''')

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.415, rely=0.128, height=60, relwidth=0.348)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 20")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=self.altura)

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.415, rely=0.388, height=60, relwidth=0.348)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Courier New} -size 20")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(textvariable=self.diametro)

        self.Label3_1 = tk.Label(self.Frame1)
        self.Label3_1.place(relx=0.452, rely=-0.252, height=78, width=165)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(anchor='w')
        self.Label3_1.configure(background="#252a40")
        self.Label3_1.configure(compound='left')
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(font="-family {Segoe UI} -size 22")
        self.Label3_1.configure(foreground="#f2f2f2")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Diâmetro [m]:''')

        self.Label3_2 = tk.Label(self.Frame1)
        self.Label3_2.place(relx=0.145, rely=0.368, height=79, width=167)
        self.Label3_2.configure(activebackground="#f9f9f9")
        self.Label3_2.configure(anchor='w')
        self.Label3_2.configure(background="#252a40")
        self.Label3_2.configure(compound='left')
        self.Label3_2.configure(disabledforeground="#a3a3a3")
        self.Label3_2.configure(font="-family {Segoe UI} -size 22")
        self.Label3_2.configure(foreground="#f2f2f2")
        self.Label3_2.configure(highlightbackground="#d9d9d9")
        self.Label3_2.configure(highlightcolor="black")
        self.Label3_2.configure(text='''Diâmetro [m]:''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.039, rely=0.068, height=74, width=702)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#f2f2f2")
        self.Label2.configure(compound='center')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 36 -weight bold")
        self.Label2.configure(foreground="#007ef9")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Cálculo do volume''')

        self.Label3_3 = tk.Label(self.top)
        self.Label3_3.place(relx=0.716, rely=0.07, height=79, width=307)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(anchor='w')
        self.Label3_3.configure(background="#2e3349")
        self.Label3_3.configure(compound='left')
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(font="-family {Segoe UI} -size 22")
        self.Label3_3.configure(foreground="#ffffff")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''Volume:''')

        self.Button1.configure(command=self.calcular)

def start_up():
    tela_support.main()

if __name__ == '__main__':
    tela_support.main()