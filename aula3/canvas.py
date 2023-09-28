from tkinter import Tk, Label, Canvas, Button
from tkinter import messagebox as msg

tela = Tk() 
tela.geometry("900x400")
tela.title("Tela principal")

titulo1 = Label(tela, text="Desenhando no Canvas", font="Arial 12", fg="#34495e")

canvas  = Canvas(tela, bg="#34495e")

retangulo = canvas.create_rectangle(100, 100, 200, 200, outline= "black", fill="white", width=2)  

circulo   = canvas.create_oval(50, 50, 100, 100, outline="white", fill="red", width=2)

def esticar():
		canvas.coords(retangulo, 100, 100, 300, 200)
                
def mover():
    canvas.move(retangulo, 0, 10)
    canvas.moveto(circulo, 150, 150)

botao = Button(tela, text="Alterar", font="Arial 12", command=lambda:mover())

titulo1.pack()
canvas.pack()
botao.pack()

tela.mainloop()