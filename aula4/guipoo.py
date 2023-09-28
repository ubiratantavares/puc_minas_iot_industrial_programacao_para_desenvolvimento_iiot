import tkinter
from tkinter import *
from tkinter import messagebox as msg
import time


class Bargraph():
    def __init__(self,tela):
        self.label=[0,0,0,0]
        for i in range(4):
            self.label[i]  = Label(tela, text="__", font="Arial 22", bg="#34495e",fg="#34495e")

    def alterar(self, valor):
        valor = int( 4*float(valor)/100  )
        for i in range(4):
            self.label[i].configure(bg="#34495e",fg="#34495e")
        for i in range(valor):
            self.label[i].configure(bg="red",fg="red")

    def posicionar(self):
        for i in [3,2,1,0]:
           self.label[i].pack()


if __name__ == '__main__':

    tela = Tk() 
    tela.geometry("900x400")
    tela.title("Tela principal")

    num = StringVar()

    titulo1 = Label(tela, text="Bargraph animado", font="Arial 32", fg="#34495e")
    labelTexto = Label(tela, text="Digite um valor entre 0-100%", font="Arial 22")
    bargraph  = Bargraph(tela) # Aqui instanciamos o objeto bargraph
    textbox = Entry(tela, textvariable = num, font="Arial 22")
    botao   = Button(tela, text="Alterar", font="Arial 22", command=lambda:bargraph.alterar(num.get()))

    titulo1.pack()
    labelTexto.pack()
    bargraph.posicionar()

    textbox.pack()
    botao.pack()

    tela.mainloop()