import os
import time
#libreria de app/sistema 
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
#funcion salir de la app 
def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()
    
#aca van todas las clases y funciones  

def mostrar_menu():
    print("Club Deportivo")
    

#crear ventana del sistema
ventana= tk.Tk()
ventana.config(width=600,height=600)
ventana.title("Club Deportivo - Los tres Mosqueteros")
#crear barra de menu
barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)
menu_Registro= Menu(barra_menu)
menu_Pagar= Menu(barra_menu)
menu_Inscribir= Menu(barra_menu)

#menu 1
menu_Registro.add_command(label="Nuevo Socio", command=mostrar_menu)
menu_Registro.add_command(label="Nuevo No Socio", command=mostrar_menu)
menu_Registro.add_command(label="Nuevo Invitado", command=mostrar_menu)
barra_menu.add_cascade(label="Registro", menu=menu_Registro)

#menu 2
menu_Pagar.add_command(label="Pagar Socio", command=mostrar_menu)
menu_Pagar.add_command(label="Pagar No Socio", command=mostrar_menu)
menu_Pagar.add_command(label="Pagar Invitado", command=mostrar_menu)
barra_menu.add_cascade(label="Pagar", menu=menu_Pagar)

#menu 3
menu_Inscribir.add_command(label="Inscribir Socio", command=mostrar_menu)
menu_Inscribir.add_command(label="Inscribir No Socio", command=mostrar_menu)
menu_Inscribir.add_command(label="Inscribir Invitado", command=mostrar_menu)
barra_menu.add_cascade(label="Inscribir a Deporte", menu=menu_Inscribir)

#menu 4
menu_ayuda= Menu(barra_menu)
menu_ayuda.add_command(label="Rendicion de cuentas", command=mostrar_menu)
menu_ayuda.add_command(label="Salir", command=funcion_salir)
barra_menu.add_cascade(label="Soporte", menu=menu_ayuda)



ventana.mainloop() 