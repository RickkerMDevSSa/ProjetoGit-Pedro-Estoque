from tkinter import *
import tkinter as tk
from tkinter import Tk, font 
from inclusao import incluir
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk() 
# Barra do menu
root.title("Controle de Clientes")
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label="Ajuda")
filemenu.add_command(label="Encerrar programa")
filemenu.add_command(label="Preferências")
menubar.add_cascade(label="Opções", menu=filemenu)
root.config(menu=menubar) #sem isso ele não aparece

#Tamanho e background
root.geometry("850x620") 

bg = PhotoImage(file = "b.png") 
canvas1 = Canvas( root, width = 100, height = 100) 
canvas1.pack(fill = "both", expand = True) 
canvas1.create_image( 0, 0, image = bg,  anchor = "nw") #NW é a posição

#Menu Iniciar
Iniciar = Label(text="MENU",bg="white",foreground='#f07241',relief=RIDGE).place(x=200, y=200)

#Opções
Adcionar = Button(text="Adcionar Cliente",bg="#f07241",foreground='WHITE',relief=RIDGE,command= incluir).place(x=200, y=230)
Alterar = Button(text="Alterar Cliente", bg="#f07241",foreground='WHITE',relief=RIDGE).place(x=200, y=260)
Excluir = Button(text="Excluir Cliente", bg="#f07241",foreground='WHITE',relief=RIDGE).place(x=200, y=290)
Relatório = Button(text="Relatório", bg="#f07241",foreground='WHITE',relief=RIDGE).place(x=200, y=320)

final = Button(root,text="Encerrar",bg="white",foreground='#c04848',relief=RIDGE,command=root.destroy).place(x=200, y=350)
root.resizable(FALSE,FALSE)
root.mainloop() 