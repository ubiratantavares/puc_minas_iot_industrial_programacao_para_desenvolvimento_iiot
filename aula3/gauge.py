from tkinter import Tk, PhotoImage, Label
from threading import Thread
import time

tela = Tk()

tela.geometry("900x900")
tela.title("Animação Gauge")
titulo = Label(tela, text="Animação com Thread", font="Arial 12", fg="#3498db")
label = Label(tela, font="Arial 12", fg="#34495e")
titulo.pack()
label.pack()

imagens = []

for i in range(4):
    imagens.append(PhotoImage(file="../aula3/imagens/gauge"+str(i+1)+".png"))


def executar():
    cont = 0
    while True:
        label.configure(image=imagens[cont])  # 0, 1, 2, 3
        time.sleep(1)
        if cont == 3:
            cont = 0
        else:
            cont += 1


thread = Thread(target=executar, daemon=True)
thread.start()

tela.mainloop()
