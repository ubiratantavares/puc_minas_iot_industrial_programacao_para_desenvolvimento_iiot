#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Nov 02, 2023 12:24:31 AM -03  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import principal_support

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

class Principal:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+2183+519")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("Principal")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.txtLogin = tk.StringVar()
        self.txtSenha = tk.StringVar()

        self.btnEnviar = tk.Button(self.top)
        self.btnEnviar.place(relx=0.367, rely=0.422, height=34, width=147)
        self.btnEnviar.configure(activebackground="beige")
        self.btnEnviar.configure(activeforeground="#ffffff")
        self.btnEnviar.configure(background="#0080ff")
        self.btnEnviar.configure(command=principal_support.cliquebtnEnviar)
        self.btnEnviar.configure(compound='center')
        self.btnEnviar.configure(disabledforeground="#a3a3a3")
        self.btnEnviar.configure(font="-family {Segoe UI} -size 16")
        self.btnEnviar.configure(foreground="#ffffff")
        self.btnEnviar.configure(highlightbackground="#d9d9d9")
        self.btnEnviar.configure(highlightcolor="#ffffff")
        self.btnEnviar.configure(pady="0")
        self.btnEnviar.configure(text='''Enviar''')
        self.btnEnviar.bind('<Button-1>',lambda e:principal_support.clique_btnEnviar(e))
        self.lblLogin = tk.Label(self.top)
        self.lblLogin.place(relx=0.433, rely=0.067, height=41, width=74)
        self.lblLogin.configure(activebackground="#f9f9f9")
        self.lblLogin.configure(anchor='w')
        self.lblLogin.configure(background="#ffffff")
        self.lblLogin.configure(compound='center')
        self.lblLogin.configure(disabledforeground="#a3a3a3")
        self.lblLogin.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.lblLogin.configure(foreground="#000000")
        self.lblLogin.configure(highlightbackground="#d9d9d9")
        self.lblLogin.configure(highlightcolor="black")
        self.lblLogin.configure(text='''Login''')
        self.txtLogin = tk.Entry(self.top)
        self.txtLogin.place(relx=0.3, rely=0.156, height=20, relwidth=0.423)
        self.txtLogin.configure(background="white")
        self.txtLogin.configure(disabledforeground="#a3a3a3")
        self.txtLogin.configure(font="-family {Courier New} -size 16")
        self.txtLogin.configure(foreground="#000000")
        self.txtLogin.configure(highlightbackground="#d9d9d9")
        self.txtLogin.configure(highlightcolor="black")
        self.txtLogin.configure(insertbackground="black")
        self.txtLogin.configure(selectbackground="#c4c4c4")
        self.txtLogin.configure(selectforeground="black")
        self.txtLogin.configure(textvariable=self.txtLogin)
        self.lblSenha = tk.Label(self.top)
        self.lblSenha.place(relx=0.433, rely=0.244, height=41, width=74)
        self.lblSenha.configure(activebackground="#f9f9f9")
        self.lblSenha.configure(anchor='w')
        self.lblSenha.configure(background="#ffffff")
        self.lblSenha.configure(compound='center')
        self.lblSenha.configure(disabledforeground="#a3a3a3")
        self.lblSenha.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.lblSenha.configure(foreground="#000000")
        self.lblSenha.configure(highlightbackground="#d9d9d9")
        self.lblSenha.configure(highlightcolor="black")
        self.lblSenha.configure(text='''Senha''')
        self.txtSenha = tk.Entry(self.top)
        self.txtSenha.place(relx=0.3, rely=0.333, height=20, relwidth=0.423)
        self.txtSenha.configure(background="white")
        self.txtSenha.configure(disabledforeground="#a3a3a3")
        self.txtSenha.configure(font="-family {Courier New} -size 16")
        self.txtSenha.configure(foreground="#000000")
        self.txtSenha.configure(highlightbackground="#d9d9d9")
        self.txtSenha.configure(highlightcolor="black")
        self.txtSenha.configure(insertbackground="black")
        self.txtSenha.configure(selectbackground="#c4c4c4")
        self.txtSenha.configure(selectforeground="black")
        self.txtSenha.configure(textvariable=self.txtSenha)

def start_up():
    principal_support.main()

if __name__ == '__main__':
    principal_support.main()



