from tkinter import *
from tkinter import messagebox as msg
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("chave1.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://profpedrohj-1fffe-default-rtdb.firebaseio.com'
})

tela = Tk() 
tela.geometry("500x300")
tela.title("Firebase")
campo = StringVar() # Declaramos a StringVar valor
valor = StringVar() # Declaramos a StringVar valor

texto1  = Label(tela, text="Firebase" , font="Arial 28").pack() 
lbCampo  = Label(tela, text="Digite o sensor" , font="Arial 18").pack() 
caixa1  = Entry(tela,  textvariable=campo, font="Arial 22").pack()
lbValor  = Label(tela, text="Digite o valor" , font="Arial 18").pack() 
caixa2  = Entry(tela,  textvariable=valor, font="Arial 22").pack()

def clique():
    ref = db.reference('sensores/'+campo.get() )
    ref.set(float(valor.get())) 
    msg.showinfo("Mensagem","Alterado com sucesso")

botao   = Button(tela, text="Alterar", font="Arial 22", command=clique).pack()

tela.mainloop()