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
valor = StringVar() # Declaramos a StringVar valor

texto1  = Label(tela, text="Consultar Firebase" , font="Arial 28").pack() 
caixa1  = Entry(tela,  textvariable=valor, font="Arial 22").pack()

def clique():
    ref = db.reference('sensores/'+valor.get() ) 
    data = ref.get()
    msg.showinfo("Valor: ", str(data))
    print(data)

botao   = Button(tela, text="Buscar", font="Arial 22", command=clique).pack()

tela.mainloop()