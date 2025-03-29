import tkinter as tk 
from tkinter import messagebox  
import random  

def simular():
    try:
        num_sorteos = int(entry_sorteos.get())
        
        mi_numero = int(entry_mi_numero.get().strip())
        
        if num_sorteos <= 0 or mi_numero < 1 or mi_numero > 100:
            raise ValueError("Ingrese valores válidos: un número de sorteos positivo y un número de participante entre 1 y 100")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido de sorteos y un número de participante (1-100)")
        return
    
    participantes = list(range(1, 101)) 
    veces_juez = 0  
    num_jueces_por_sorteo = 10  
    
    resultados_texto = "Resultados de cada sorteo:\n"
    
    # Bucle para realizar los sorteos
    for i in range(1, num_sorteos + 1):
        jueces = random.sample(participantes, num_jueces_por_sorteo)  
        if mi_numero in jueces:  
            veces_juez += 1  
        
        porcentaje_exito_parcial = (veces_juez / i) * 100  
        resultados_texto += f"Sorteo {i}: {'Juez' if mi_numero in jueces else 'No juez'} - {porcentaje_exito_parcial:.2f}% éxito acumulado\n"
    
    porcentaje_exito = (veces_juez / num_sorteos) * 100  
    resultados_texto += f"\nEl participante {mi_numero} fue juez {veces_juez} veces ({porcentaje_exito:.2f}% de éxito en total).\n"
    
    text_resultados.delete("1.0", tk.END)  
    text_resultados.insert(tk.END, resultados_texto)  
    
# Configuración de la interfaz gráfica
top = tk.Tk() 
top.title("Simulación de Jueces - Método Montecarlo")  #

tk.Label(top, text="Número de sorteos:").pack() 
entry_sorteos = tk.Entry(top)  
entry_sorteos.pack()

tk.Label(top, text="Número de participante con el que jugarás:").pack()  
entry_mi_numero = tk.Entry(top)  
entry_mi_numero.pack()

btn_simular = tk.Button(top, text="Simular", command=simular)  
btn_simular.pack()

text_resultados = tk.Text(top, height=20, width=60) 
text_resultados.pack()

top.mainloop()  