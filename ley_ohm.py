import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

def calcular_resistencia():
    v = random.randint(1, 220)
    i = random.randint(1, 10)
    r = v / i
    mv = f"EL voltaje es {v} V\n"
    mi = f"La corriente es {i} A\n"
    mr = f"La resistencia es {r:.2f} Ohm\n\n"
    texto.insert(tk.END, mv)
    texto.insert(tk.END, mi)
    texto.insert(tk.END, mr)
    return r

def limpiar():
    texto.delete("1.0", tk.END)


root = tk.Tk()
root.title("Ley de Ohm")
root.geometry("300x150")

marco = ttk.LabelFrame(root, text="Ley de Ohm")
marco.pack()

button = ttk.Button(root, text="Calcular resistencia", command=calcular_resistencia)
button.pack()

button_limpiar = ttk.Button(root, text="Limpiar", command=limpiar)
button_limpiar.pack()

texto = tk.Text(root, width=30, height=10)
texto.pack()

root.mainloop()
