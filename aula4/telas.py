# Autor: Prof. Pedro H.J
# Data: 28/11/22
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import telas_support

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

class tela1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("928x736+394+243")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#0f3d5c")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Label1_1 = tk.Label(self.top)
        self.Label1_1.place(relx=0.119, rely=0.054, height=51, width=1055)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#0f3d5c")
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Bahnschrift Light Condensed} -size 48")
        self.Label1_1.configure(foreground="#ffffff")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Sistema de Monitoramento IIOT''')

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.086, rely=0.313, relheight=0.577
                , relwidth=0.361)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(self.Frame1)
        self.Canvas1.place(relx=0.179, rely=0.071, relheight=0.706
                , relwidth=0.597)
        self.Canvas1.configure(background="#6c66db")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.209, rely=0.824, height=51, width=204)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Bahnschrift Light Condensed} -size 48")
        self.Label1.configure(foreground="#0f3d5c")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(justify='left')
        self.Label1.configure(text='''Tanque 1''')

        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.496, rely=0.313, relheight=0.183
                , relwidth=0.373)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="8")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#0f3d5c")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.lbNivel = tk.Label(self.Frame2)
        self.lbNivel.place(relx=0.26, rely=0.222, height=71, width=214)
        self.lbNivel.configure(activebackground="#f9f9f9")
        self.lbNivel.configure(anchor='w')
        self.lbNivel.configure(background="#0f3d5c")
        self.lbNivel.configure(compound='left')
        self.lbNivel.configure(disabledforeground="#a3a3a3")
        self.lbNivel.configure(font="-family {Bahnschrift Light Condensed} -size 48")
        self.lbNivel.configure(foreground="#ffffff")
        self.lbNivel.configure(highlightbackground="#d9d9d9")
        self.lbNivel.configure(highlightcolor="black")
        self.lbNivel.configure(text='''00 L''')

        self.Frame2_1 = tk.Frame(self.top)
        self.Frame2_1.place(relx=0.496, rely=0.53, relheight=0.346
                , relwidth=0.373)
        self.Frame2_1.configure(relief='groove')
        self.Frame2_1.configure(borderwidth="2")
        self.Frame2_1.configure(relief="groove")
        self.Frame2_1.configure(background="#ffffff")
        self.Frame2_1.configure(highlightbackground="#d9d9d9")
        self.Frame2_1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame2_1)
        self.Label1.place(relx=0.145, rely=0.118, height=221, width=254)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        photo_location = os.path.join(_location,"PUC.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)

        self.Label1_1_1 = tk.Label(self.top)
        self.Label1_1_1.place(relx=0.647, rely=0.177, height=50, width=943)
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(anchor='w')
        self.Label1_1_1.configure(background="#0f3d5c")
        self.Label1_1_1.configure(compound='left')
        self.Label1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1.configure(font="-family {Bahnschrift Light Condensed} -size 24")
        self.Label1_1_1.configure(foreground="#ffffff")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="black")
        self.Label1_1_1.configure(text='''Prof. MSc. Pedro H.J''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1_1_1_1 = tk.Label(self.top)
        self.Label1_1_1_1.place(relx=0.097, rely=0.19, height=31, width=176)
        self.Label1_1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1_1.configure(anchor='w')
        self.Label1_1_1_1.configure(background="#0f3d5c")
        self.Label1_1_1_1.configure(compound='left')
        self.Label1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_1.configure(font="-family {Bahnschrift Light Condensed} -size 24")
        self.Label1_1_1_1.configure(foreground="#ffffff")
        self.Label1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_1.configure(highlightcolor="black")
        self.Label1_1_1_1.configure(text='''Disciplina PDI''')

def start_up():
    telas_support.main()

if __name__ == '__main__':
    telas_support.main()