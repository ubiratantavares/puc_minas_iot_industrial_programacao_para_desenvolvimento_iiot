from tkinter import *

def janela1():
    tela = Tk() 
    tela.geometry("900x500")
    tela.title("Tela principal")

    nome = StringVar() # Declaramos a StringVar nome

    logo = PhotoImage(file="aula3/imagens/PUC.png")

    imagem = Label(tela, image=logo)
    imagem.pack()

    texto1 = Label(tela, text="Tela Principal" , font="Arial 12")
    texto1.pack()

    caixa1 = Entry(tela,  textvariable=nome, font="Arial 12")
    caixa1.pack()

    def clique():
        print(f'Seja bem-vindo, {nome.get()}') 

    botao = Button(tela, text="Salvar", font="Arial 12", command=clique)
    botao.pack()

    tela.mainloop()

def janela2():
    tela = Tk()

    tela.geometry("600x600")
    tela.title("Tela Principal")

    texto1 = Label(tela, text="Tela Principal", font="Arial 12")
    caixa1 = Entry(tela, font="Arial 12")
    botao1 = Button(tela, text="Salvar", font="Arial 12")

    texto1.grid(row=0, column=0)
    caixa1.grid(row=1, column=1)
    botao1.grid(row=1, column=2)

    tela.mainloop()  

def janela3():
    tela = Tk()

    tela.geometry("600x600")    
    tela.title("Tela Principal")

    texto1 = Label(tela, text="Tela Principal", font="Arial 12")
    caixa1 = Entry(tela, font="Arial 12")
    botao1 = Button(tela, text="Salvar", font="Arial 12")

    texto1.place(x=250, y=0)
    caixa1.place(x=250, y=150)
    botao1.place(x=350, y=250)

    tela.mainloop()    


if __name__ == '__main__':
    janela1()
    #janela2()
    #janela3()

 