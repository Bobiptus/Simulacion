import tkinter as tk
from tkinter import messagebox

def incrementar():
    global contador
    contador += 1
    mostrar_contador()

def restar():
    global contador
    contador -= 1
    mostrar_contador()

def mostrar_contador():
    mostrar.delete("1.0", tk.END)  
    mostrar.insert(tk.END, str(contador))  

contador = 0

root = tk.Tk()
root.title("Contador de personas")
root.geometry("300x200")

marco = tk.Frame(root)
marco.pack()

button_sumar = tk.Button(root, text="Sumar", command=incrementar)
button_sumar.pack()

button_restar = tk.Button(root, text="Restar", command=restar)
button_restar.pack()

mostrar = tk.Text(root, width=10, height=1, font="Helvetica 14")
mostrar.pack()

mostrar_contador()  # Para que muestre el contador al iniciar

root.mainloop()
