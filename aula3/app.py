if __name__ == '__main__':
    
    from tkinter import *
    from tkinter import messagebox as msg

    tela = Tk() 
    tela.geometry("500x300")
    tela.title("Tela principal")

    tensao   = StringVar()
    potencia = StringVar()

    def clique():
        potencia_nominal = float(potencia.get())
        tensao_nominal = float(tensao.get())
        corrente_nominal = potencia_nominal/tensao_nominal
        msg.showinfo("Corrente Nominal", f"{corrente_nominal:.2f}" + " A" )

    titulo1 = Label(tela, text="Corrente Elétrica", font="Arial 12", bg="#3498db",fg="#ecf0f1")
    label1  = Label(tela, text="Potência elétrica [W]:", font="Arial 12", fg="#34495e")
    caixa1  = Entry(tela,  textvariable=potencia, font="Arial 12")
    label2  = Label(tela, text="Tensão elétrica   [V]:", font="Arial 12", fg="#34495e")
    caixa2  = Entry(tela,  textvariable=tensao, font="Arial 12")
    botao   = Button(tela, text="Calcular", font="Arial 12", fg="#ecf0f1", bg="#27ae60", command=clique)

    titulo1.pack()
    label1.pack()
    caixa1.pack()
    label2.pack()
    caixa2.pack()
    botao.pack()

    tela.mainloop()