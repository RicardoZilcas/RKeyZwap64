import tkinter as tk
from tkinter import messagebox
import pyperclip

from rkeyzwap64 import cifrar_doble, descifrar_doble

# Crear ventana principal
ventana = tk.Tk()
ventana.title("RKeyZwap64")
ventana.geometry("500x400")
ventana.resizable(False, False)

# Título
titulo = tk.Label(ventana, text="🔐 RKeyZwap64", font=("Segoe UI", 20, "bold"))
titulo.pack(pady=10)

# Campo de entrada
entrada_label = tk.Label(ventana, text="Escribe tu mensaje:")
entrada_label.pack()
entrada_texto = tk.Text(ventana, height=4, width=60)
entrada_texto.pack(pady=5)

# Campo de resultado
resultado_label = tk.Label(ventana, text="Resultado:")
resultado_label.pack()
resultado_texto = tk.Text(ventana, height=4, width=60, state='disabled')
resultado_texto.pack(pady=5)

# Funciones
def codificar():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Advertencia", "Por favor escribe un mensaje.")
        return
    resultado = cifrar_doble(texto)
    mostrar_resultado(resultado)

def decodificar():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Advertencia", "Por favor escribe un mensaje.")
        return
    resultado = descifrar_doble(texto)
    mostrar_resultado(resultado)

def copiar_resultado():
    texto = resultado_texto.get("1.0", tk.END).strip()
    if texto:
        pyperclip.copy(texto)
        messagebox.showinfo("Copiado", "Resultado copiado al portapapeles.")

def mostrar_resultado(resultado):
    resultado_texto.config(state='normal')
    resultado_texto.delete("1.0", tk.END)
    resultado_texto.insert(tk.END, resultado)
    resultado_texto.config(state='disabled')

# Botones
botones_frame = tk.Frame(ventana)
botones_frame.pack(pady=10)

btn_codificar = tk.Button(botones_frame, text="Codificar", command=codificar, bg="#00c853", fg="white", width=15)
btn_codificar.pack(side=tk.LEFT, padx=10)

btn_decodificar = tk.Button(botones_frame, text="Decodificar", command=decodificar, bg="#2962ff", fg="white", width=15)
btn_decodificar.pack(side=tk.LEFT, padx=10)

btn_copiar = tk.Button(ventana, text="Copiar Resultado", command=copiar_resultado, bg="#ff6f00", fg="white", width=30)
btn_copiar.pack(pady=10)

# Créditos
creditos = tk.Label(ventana, text="Creado por Zilcas 🧠 con ayuda de ChatGPT-4o", font=("Segoe UI", 10))
creditos.pack(pady=5)

ventana.mainloop()
