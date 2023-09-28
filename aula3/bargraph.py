from tkinter import *
from tkinter import messagebox as msg

tela = Tk() 

tela.geometry("900x400")
tela.title("Tela principal")

num = StringVar()

def alterar(label, valor):
    valor = int(4*float(valor)/100 )
    for i in range(4):
        label[i].configure(bg="#34495e", fg="#34495e")
    for i in range(valor):
        label[i].configure(bg="red", fg="red")

titulo1 = Label(tela, text="Bargraph Animado", font="Arial 12", fg="#34495e")

label = [0,0,0,0]

labelTexto = Label(tela, text="Digite um valor entre 0-100%", font="Arial 12")

for i in range(4):
    label[i] = Label(tela, text="__", font="Arial 12", bg="#34495e", fg="#34495e")

textbox = Entry(tela, textvariable=num, font="Arial 12")

botao = Button(tela, text="Alterar", font="Arial 12", command=lambda:alterar(label, num.get()))

titulo1.pack()

for i in [3,2,1,0]:
    label[i].pack()
    
labelTexto.pack()
textbox.pack()
botao.pack()

tela.mainloop()