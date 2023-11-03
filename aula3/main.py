from tkinter import Tk, Label, Canvas, Button, PhotoImage

tela = Tk()

tela.geometry("900x500")
tela.title("Desenho no Canvas")

titulo = Label(tela, text="Desenho com python", font="Arial 32", fg="#333333")
canvas = Canvas(tela, bg="#888888")

def mover():
    canvas.move(retangulo, 5, 5) # relativo para baixo
    #canvas.moveto(circulo, 60, 100) # absoluto
    print("Movendo...")

def aumentar():
    canvas.coords(retangulo, 10, 10, 100, 200)
    print("Aumentando...")

def diminuir():
    canvas.coords(retangulo, 10, 10, 100, 100)
    print("Diminuindo...")

img = PhotoImage(file="imagens/PUC.png")
logoPUC = canvas.create_image(120, 120, image=img)
circulo = canvas.create_oval(60, 60, 150, 150, fill="red")
retangulo = canvas.create_rectangle(10, 10, 100, 100, outline="black", fill="blue")
botao = Button(tela, text="Mover", font="Arial 22", bg="#999999", fg="#000000", command=mover)
botao2 = Button(tela, text="Aumentar", font="Arial 22", bg="#999999", fg="#000000", command=aumentar)
botao3 = Button(tela, text="Diminuir", font="Arial 22", bg="#999999", fg="#000000", command=diminuir)

titulo.pack()
canvas.pack()
botao.pack()
botao2.pack()
botao3.pack()

tela.mainloop()