#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Nov 02, 2023 11:03:12 AM -03  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import projeto_support

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

class TelaPrincipal:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("1022x854+2327+134")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("Tela Principal")
        top.configure(relief="groove")
        top.configure(background="#303030")
        top.configure(highlightbackground="#FFFFFF")
        top.configure(highlightcolor="black")

        self.top = top

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.cvsCabecalho = tk.Canvas(self.top)
        self.cvsCabecalho.place(relx=0.039, rely=0.035, relheight=0.096
                , relwidth=0.932)
        self.cvsCabecalho.configure(background="#757575")
        self.cvsCabecalho.configure(highlightbackground="#a3a3a3")
        self.cvsCabecalho.configure(highlightcolor="black")
        self.cvsCabecalho.configure(highlightthickness="0")
        self.cvsCabecalho.configure(insertbackground="black")
        self.cvsCabecalho.configure(relief="ridge")
        self.cvsCabecalho.configure(selectbackground="#c4c4c4")
        self.cvsCabecalho.configure(selectforeground="black")
        self.lblTitulo = tk.Label(self.cvsCabecalho)
        self.lblTitulo.place(relx=0.072, rely=0.244, height=52, width=283)
        self.lblTitulo.configure(activebackground="#f9f9f9")
        self.lblTitulo.configure(anchor='w')
        self.lblTitulo.configure(background="#757575")
        self.lblTitulo.configure(borderwidth="0")
        self.lblTitulo.configure(compound='left')
        self.lblTitulo.configure(disabledforeground="#000000")
        self.lblTitulo.configure(font="-family {Arial} -size 30 -weight bold")
        self.lblTitulo.configure(foreground="#ffff80")
        self.lblTitulo.configure(highlightbackground="#d9d9d9")
        self.lblTitulo.configure(highlightcolor="#000000")
        self.lblTitulo.configure(text='''SISTEMA IIOT''')
        self.lblNome = tk.Label(self.cvsCabecalho)
        self.lblNome.place(relx=0.557, rely=0.488, height=32, width=402)
        self.lblNome.configure(activebackground="#f9f9f9")
        self.lblNome.configure(anchor='w')
        self.lblNome.configure(background="#757575")
        self.lblNome.configure(compound='left')
        self.lblNome.configure(disabledforeground="#a3a3a3")
        self.lblNome.configure(font="-family {Arial} -size 20 -weight bold")
        self.lblNome.configure(foreground="#FFFFFF")
        self.lblNome.configure(highlightbackground="#d9d9d9")
        self.lblNome.configure(highlightcolor="black")
        self.lblNome.configure(text='''Aluno: Ubiratan da S.Tavares''')
        self.cvsMotor1 = tk.Canvas(self.top)
        self.cvsMotor1.place(relx=0.763, rely=0.187, relheight=0.226
                , relwidth=0.21)
        self.cvsMotor1.configure(background="#757575")
        self.cvsMotor1.configure(highlightbackground="#d9d9d9")
        self.cvsMotor1.configure(highlightcolor="black")
        self.cvsMotor1.configure(highlightthickness="0")
        self.cvsMotor1.configure(insertbackground="black")
        self.cvsMotor1.configure(relief="ridge")
        self.cvsMotor1.configure(selectbackground="#c4c4c4")
        self.cvsMotor1.configure(selectforeground="black")
        self.lblMotor1 = tk.Label(self.cvsMotor1)
        self.lblMotor1.place(relx=0.33, rely=0.073, height=26, width=91)
        self.lblMotor1.configure(activebackground="#f9f9f9")
        self.lblMotor1.configure(anchor='w')
        self.lblMotor1.configure(background="#757575")
        self.lblMotor1.configure(borderwidth="0")
        self.lblMotor1.configure(compound='center')
        self.lblMotor1.configure(disabledforeground="#a3a3a3")
        self.lblMotor1.configure(font="-family {Arial} -size 16 -weight bold")
        self.lblMotor1.configure(foreground="#ffff80")
        self.lblMotor1.configure(highlightbackground="#d9d9d9")
        self.lblMotor1.configure(highlightcolor="black")
        self.lblMotor1.configure(text='''Motor 1''')
        self.imgMotor1 = tk.Label(self.cvsMotor1)
        self.imgMotor1.place(relx=0.233, rely=0.259, height=125, width=120)
        self.imgMotor1.configure(activebackground="#f9f9f9")
        self.imgMotor1.configure(anchor='w')
        self.imgMotor1.configure(background="#757575")
        self.imgMotor1.configure(compound='left')
        self.imgMotor1.configure(disabledforeground="#a3a3a3")
        self.imgMotor1.configure(foreground="#000000")
        self.imgMotor1.configure(highlightbackground="#d9d9d9")
        self.imgMotor1.configure(highlightcolor="black")
        photo_location = os.path.join(_location,"./atividade2/images/motor1.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.imgMotor1.configure(image=_img0)
        self.cvsMotor2 = tk.Canvas(self.top)
        self.cvsMotor2.place(relx=0.763, rely=0.492, relheight=0.213
                , relwidth=0.205)
        self.cvsMotor2.configure(background="#757575")
        self.cvsMotor2.configure(highlightbackground="#d9d9d9")
        self.cvsMotor2.configure(highlightcolor="black")
        self.cvsMotor2.configure(highlightthickness="0")
        self.cvsMotor2.configure(insertbackground="black")
        self.cvsMotor2.configure(relief="ridge")
        self.cvsMotor2.configure(selectbackground="#c4c4c4")
        self.cvsMotor2.configure(selectforeground="black")
        self.lblMotor2 = tk.Label(self.cvsMotor2)
        self.lblMotor2.place(relx=0.333, rely=0.055, height=25, width=108)
        self.lblMotor2.configure(activebackground="#f9f9f9")
        self.lblMotor2.configure(anchor='w')
        self.lblMotor2.configure(background="#757575")
        self.lblMotor2.configure(borderwidth="0")
        self.lblMotor2.configure(compound='center')
        self.lblMotor2.configure(disabledforeground="#a3a3a3")
        self.lblMotor2.configure(font="-family {Arial} -size 16 -weight bold")
        self.lblMotor2.configure(foreground="#ffff80")
        self.lblMotor2.configure(highlightbackground="#d9d9d9")
        self.lblMotor2.configure(highlightcolor="black")
        self.lblMotor2.configure(text='''Motor 2''')
        self.imgMotor2 = tk.Label(self.cvsMotor2)
        self.imgMotor2.place(relx=0.238, rely=0.275, height=127, width=130)
        self.imgMotor2.configure(activebackground="#f9f9f9")
        self.imgMotor2.configure(anchor='w')
        self.imgMotor2.configure(background="#757575")
        self.imgMotor2.configure(compound='left')
        self.imgMotor2.configure(disabledforeground="#a3a3a3")
        self.imgMotor2.configure(foreground="#000000")
        self.imgMotor2.configure(highlightbackground="#d9d9d9")
        self.imgMotor2.configure(highlightcolor="black")
        photo_location = os.path.join(_location,"./atividade2/images/motor1.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.imgMotor2.configure(image=_img1)
        self.cvsTanque1 = tk.Canvas(self.top)
        self.cvsTanque1.place(relx=0.045, rely=0.781, relheight=0.133
                , relwidth=0.228)
        self.cvsTanque1.configure(background="#757575")
        self.cvsTanque1.configure(highlightbackground="#d9d9d9")
        self.cvsTanque1.configure(highlightcolor="black")
        self.cvsTanque1.configure(highlightthickness="0")
        self.cvsTanque1.configure(insertbackground="black")
        self.cvsTanque1.configure(relief="ridge")
        self.cvsTanque1.configure(selectbackground="#c4c4c4")
        self.cvsTanque1.configure(selectforeground="black")
        self.lblTanque1 = tk.Label(self.cvsTanque1)
        self.lblTanque1.place(relx=0.236, rely=0.07, height=25, width=124)
        self.lblTanque1.configure(activebackground="#f9f9f9")
        self.lblTanque1.configure(anchor='w')
        self.lblTanque1.configure(background="#757575")
        self.lblTanque1.configure(compound='left')
        self.lblTanque1.configure(disabledforeground="#a3a3a3")
        self.lblTanque1.configure(font="-family {Arial} -size 16 -weight bold")
        self.lblTanque1.configure(foreground="#ffff80")
        self.lblTanque1.configure(highlightbackground="#d9d9d9")
        self.lblTanque1.configure(highlightcolor="black")
        self.lblTanque1.configure(text='''Tanque 1''')
        self.txtVolTanque1 = tk.Label(self.cvsTanque1)
        self.txtVolTanque1.place(relx=0.245, rely=0.421, height=41, width=58)
        self.txtVolTanque1.configure(activebackground="#f9f9f9")
        self.txtVolTanque1.configure(anchor='w')
        self.txtVolTanque1.configure(background="#757575")
        self.txtVolTanque1.configure(borderwidth="0")
        self.txtVolTanque1.configure(compound='left')
        self.txtVolTanque1.configure(disabledforeground="#a3a3a3")
        self.txtVolTanque1.configure(font="-family {Arial} -size 30 -weight bold")
        self.txtVolTanque1.configure(foreground="#ffffff")
        self.txtVolTanque1.configure(highlightbackground="#d9d9d9")
        self.txtVolTanque1.configure(highlightcolor="black")
        self.txtVolTanque1.configure(text='''66''')
        self.txtMetroTanque1 = tk.Label(self.cvsTanque1)
        self.txtMetroTanque1.place(relx=0.541, rely=0.491, height=25, width=36)
        self.txtMetroTanque1.configure(activebackground="#f9f9f9")
        self.txtMetroTanque1.configure(anchor='w')
        self.txtMetroTanque1.configure(background="#757575")
        self.txtMetroTanque1.configure(borderwidth="0")
        self.txtMetroTanque1.configure(compound='left')
        self.txtMetroTanque1.configure(disabledforeground="#a3a3a3")
        self.txtMetroTanque1.configure(font="-family {Arial} -size 24 -weight bold")
        self.txtMetroTanque1.configure(foreground="#ffffff")
        self.txtMetroTanque1.configure(highlightbackground="#d9d9d9")
        self.txtMetroTanque1.configure(highlightcolor="black")
        self.txtMetroTanque1.configure(text='''m''')
        self.txtCuboTanque1 = tk.Label(self.cvsTanque1)
        self.txtCuboTanque1.place(relx=0.687, rely=0.351, height=25, width=36)
        self.txtCuboTanque1.configure(activebackground="#f9f9f9")
        self.txtCuboTanque1.configure(anchor='w')
        self.txtCuboTanque1.configure(background="#757575")
        self.txtCuboTanque1.configure(borderwidth="0")
        self.txtCuboTanque1.configure(compound='left')
        self.txtCuboTanque1.configure(disabledforeground="#a3a3a3")
        self.txtCuboTanque1.configure(font="-family {Arial} -size 24 -weight bold")
        self.txtCuboTanque1.configure(foreground="#ffffff")
        self.txtCuboTanque1.configure(highlightbackground="#d9d9d9")
        self.txtCuboTanque1.configure(highlightcolor="black")
        self.txtCuboTanque1.configure(text='''3''')
        self.cvsTanque2 = tk.Canvas(self.top)
        self.cvsTanque2.place(relx=0.302, rely=0.781, relheight=0.133
                , relwidth=0.226)
        self.cvsTanque2.configure(background="#757575")
        self.cvsTanque2.configure(highlightbackground="#d9d9d9")
        self.cvsTanque2.configure(highlightcolor="black")
        self.cvsTanque2.configure(highlightthickness="0")
        self.cvsTanque2.configure(insertbackground="black")
        self.cvsTanque2.configure(relief="ridge")
        self.cvsTanque2.configure(selectbackground="#c4c4c4")
        self.cvsTanque2.configure(selectforeground="black")
        self.lblTanque2 = tk.Label(self.cvsTanque2)
        self.lblTanque2.place(relx=0.234, rely=0.07, height=25, width=123)
        self.lblTanque2.configure(activebackground="#f9f9f9")
        self.lblTanque2.configure(anchor='w')
        self.lblTanque2.configure(background="#757575")
        self.lblTanque2.configure(compound='left')
        self.lblTanque2.configure(disabledforeground="#a3a3a3")
        self.lblTanque2.configure(font="-family {Arial} -size 16 -weight bold")
        self.lblTanque2.configure(foreground="#ffff80")
        self.lblTanque2.configure(highlightbackground="#d9d9d9")
        self.lblTanque2.configure(highlightcolor="black")
        self.lblTanque2.configure(text='''Tanque 2''')
        self.txtVolTanque2 = tk.Label(self.cvsTanque2)
        self.txtVolTanque2.place(relx=0.247, rely=0.421, height=41, width=59)
        self.txtVolTanque2.configure(activebackground="#f9f9f9")
        self.txtVolTanque2.configure(anchor='w')
        self.txtVolTanque2.configure(background="#757575")
        self.txtVolTanque2.configure(borderwidth="0")
        self.txtVolTanque2.configure(compound='left')
        self.txtVolTanque2.configure(disabledforeground="#a3a3a3")
        self.txtVolTanque2.configure(font="-family {Arial} -size 30 -weight bold")
        self.txtVolTanque2.configure(foreground="#ffffff")
        self.txtVolTanque2.configure(highlightbackground="#d9d9d9")
        self.txtVolTanque2.configure(highlightcolor="black")
        self.txtVolTanque2.configure(text='''95''')
        self.txtMetroTanque2 = tk.Label(self.cvsTanque2)
        self.txtMetroTanque2.place(relx=0.545, rely=0.491, height=25, width=36)
        self.txtMetroTanque2.configure(activebackground="#f9f9f9")
        self.txtMetroTanque2.configure(anchor='w')
        self.txtMetroTanque2.configure(background="#757575")
        self.txtMetroTanque2.configure(borderwidth="0")
        self.txtMetroTanque2.configure(compound='left')
        self.txtMetroTanque2.configure(disabledforeground="#a3a3a3")
        self.txtMetroTanque2.configure(font="-family {Arial} -size 24 -weight bold")
        self.txtMetroTanque2.configure(foreground="#ffffff")
        self.txtMetroTanque2.configure(highlightbackground="#d9d9d9")
        self.txtMetroTanque2.configure(highlightcolor="black")
        self.txtMetroTanque2.configure(text='''m''')
        self.txtCuboTanque2 = tk.Label(self.cvsTanque2)
        self.txtCuboTanque2.place(relx=0.654, rely=0.351, height=25, width=37)
        self.txtCuboTanque2.configure(activebackground="#f9f9f9")
        self.txtCuboTanque2.configure(anchor='w')
        self.txtCuboTanque2.configure(background="#757575")
        self.txtCuboTanque2.configure(borderwidth="0")
        self.txtCuboTanque2.configure(compound='left')
        self.txtCuboTanque2.configure(disabledforeground="#a3a3a3")
        self.txtCuboTanque2.configure(font="-family {Arial} -size 24 -weight bold")
        self.txtCuboTanque2.configure(foreground="#ffffff")
        self.txtCuboTanque2.configure(highlightbackground="#d9d9d9")
        self.txtCuboTanque2.configure(highlightcolor="black")
        self.txtCuboTanque2.configure(text='''3''')
        self.cvsBotoes = tk.Canvas(self.top)
        self.cvsBotoes.place(relx=0.56, rely=0.781, relheight=0.133
                , relwidth=0.194)
        self.cvsBotoes.configure(background="#757575")
        self.cvsBotoes.configure(highlightbackground="#d9d9d9")
        self.cvsBotoes.configure(highlightcolor="black")
        self.cvsBotoes.configure(highlightthickness="0")
        self.cvsBotoes.configure(insertbackground="black")
        self.cvsBotoes.configure(relief="ridge")
        self.cvsBotoes.configure(selectbackground="#c4c4c4")
        self.cvsBotoes.configure(selectforeground="black")
        self.btnAlerta = tk.Button(self.cvsBotoes)
        self.btnAlerta.place(relx=0.152, rely=0.175, height=34, width=134)
        self.btnAlerta.configure(activebackground="beige")
        self.btnAlerta.configure(activeforeground="black")
        self.btnAlerta.configure(background="#d9d9d9")
        self.btnAlerta.configure(compound='left')
        self.btnAlerta.configure(disabledforeground="#a3a3a3")
        self.btnAlerta.configure(font="-family {Arial} -size 12 -weight bold")
        self.btnAlerta.configure(foreground="#000000")
        self.btnAlerta.configure(highlightbackground="#d9d9d9")
        self.btnAlerta.configure(highlightcolor="black")
        self.btnAlerta.configure(pady="0")
        self.btnAlerta.configure(text='''Config. Alerta''')
        self.btnAlerta.bind('<Button-1>',lambda e:projeto_support.alertar(e))
        self.btnGrafico = tk.Button(self.cvsBotoes)
        self.btnGrafico.place(relx=0.152, rely=0.614, height=34, width=137)
        self.btnGrafico.configure(activebackground="beige")
        self.btnGrafico.configure(activeforeground="black")
        self.btnGrafico.configure(background="#d9d9d9")
        self.btnGrafico.configure(compound='left')
        self.btnGrafico.configure(disabledforeground="#a3a3a3")
        self.btnGrafico.configure(font="-family {Arial} -size 12 -weight bold")
        self.btnGrafico.configure(foreground="#000000")
        self.btnGrafico.configure(highlightbackground="#d9d9d9")
        self.btnGrafico.configure(highlightcolor="black")
        self.btnGrafico.configure(pady="0")
        self.btnGrafico.configure(text='''Gráficos''')
        self.btnGrafico.bind('<Button-1>',lambda e:projeto_support.plotar(e))
        self.imgInstituicao = tk.Label(self.top)
        self.imgInstituicao.place(relx=0.841, rely=0.738, height=174, width=168)
        self.imgInstituicao.configure(activebackground="#f9f9f9")
        self.imgInstituicao.configure(anchor='w')
        self.imgInstituicao.configure(background="#303030")
        self.imgInstituicao.configure(compound='left')
        self.imgInstituicao.configure(disabledforeground="#a3a3a3")
        self.imgInstituicao.configure(foreground="#000000")
        self.imgInstituicao.configure(highlightbackground="#d9d9d9")
        self.imgInstituicao.configure(highlightcolor="black")
        photo_location = os.path.join(_location,"./atividade2/images/PUC2.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.imgInstituicao.configure(image=_img2)
        self.lblDisciplina = tk.Label(self.top)
        self.lblDisciplina.place(relx=0.763, rely=0.948, height=29, width=206)
        self.lblDisciplina.configure(activebackground="#f9f9f9")
        self.lblDisciplina.configure(anchor='w')
        self.lblDisciplina.configure(background="#303030")
        self.lblDisciplina.configure(compound='left')
        self.lblDisciplina.configure(disabledforeground="#a3a3a3")
        self.lblDisciplina.configure(font="-family {Arial} -size 20 -weight bold")
        self.lblDisciplina.configure(foreground="#FFFFFF")
        self.lblDisciplina.configure(highlightbackground="#d9d9d9")
        self.lblDisciplina.configure(highlightcolor="black")
        self.lblDisciplina.configure(text='''Disciplina: PDI''')
        self.cvcTanques = tk.Canvas(self.top)
        self.cvcTanques.place(relx=0.035, rely=0.187, relheight=0.515
                , relwidth=0.626)
        self.cvcTanques.configure(background="#757575")
        self.cvcTanques.configure(highlightbackground="#d9d9d9")
        self.cvcTanques.configure(highlightcolor="black")
        self.cvcTanques.configure(highlightthickness="0")
        self.cvcTanques.configure(insertbackground="black")
        self.cvcTanques.configure(relief="ridge")
        self.cvcTanques.configure(selectbackground="#c4c4c4")
        self.cvcTanques.configure(selectforeground="black")
        self.cvcRetanguloAzul = tk.Canvas(self.cvcTanques)
        self.cvcRetanguloAzul.place(relx=0.313, rely=0.295, relheight=0.325
                , relwidth=0.178)
        self.cvcRetanguloAzul.configure(background="#0000ff")
        self.cvcRetanguloAzul.configure(highlightbackground="#d9d9d9")
        self.cvcRetanguloAzul.configure(highlightcolor="black")
        self.cvcRetanguloAzul.configure(highlightthickness="0")
        self.cvcRetanguloAzul.configure(insertbackground="black")
        self.cvcRetanguloAzul.configure(selectbackground="#000000")
        self.cvcRetanguloAzul.configure(selectforeground="#ffffff")
        self.cvcRetanguloBranco = tk.Canvas(self.cvcTanques)
        self.cvcRetanguloBranco.place(relx=0.548, rely=0.295, relheight=0.325
                , relwidth=0.161)
        self.cvcRetanguloBranco.configure(background="#ffffff")
        self.cvcRetanguloBranco.configure(highlightbackground="#d9d9d9")
        self.cvcRetanguloBranco.configure(highlightcolor="black")
        self.cvcRetanguloBranco.configure(highlightthickness="0")
        self.cvcRetanguloBranco.configure(insertbackground="black")
        self.cvcRetanguloBranco.configure(selectbackground="#000000")
        self.cvcRetanguloBranco.configure(selectforeground="black")
        self.imgTanques = tk.Label(self.cvcTanques)
        self.imgTanques.place(relx=0.172, rely=0.068, height=401, width=495)
        self.imgTanques.configure(activebackground="#f9f9f9")
        self.imgTanques.configure(anchor='w')
        self.imgTanques.configure(background="#757575")
        self.imgTanques.configure(borderwidth="0")
        self.imgTanques.configure(compound='left')
        self.imgTanques.configure(disabledforeground="#a3a3a3")
        self.imgTanques.configure(foreground="#000000")
        self.imgTanques.configure(highlightbackground="#d9d9d9")
        self.imgTanques.configure(highlightcolor="black")
        photo_location = os.path.join(_location,"./atividade2/images/tanques2.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.imgTanques.configure(image=_img3)

def start_up():
    projeto_support.main()

if __name__ == '__main__':
    projeto_support.main()




