
from tkinter import *
from tkinter import Toplevel

def incluir():
    janelaIncluir = Toplevel()
    janelaIncluir.geometry("300x300")
    janelaIncluir.title("Inclusão de Produtos")
    nomeProd = Label(janelaIncluir, text="Descrição do produto:")
    nomeProd.place(x=10, y=10)
    prod = Entry(janelaIncluir)
    prod.place(x=100,y=10)
    janelaIncluir.mainloop()