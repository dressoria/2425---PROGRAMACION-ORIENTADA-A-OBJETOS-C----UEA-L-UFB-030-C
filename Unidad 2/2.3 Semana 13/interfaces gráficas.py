
import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_dato():
    dato = campo_texto.get()
    if dato != "":
        lista_datos.insert(tk.END, dato)
        campo_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa un dato.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Datos")

# Crear y colocar los componentes en la ventana
etiqueta = tk.Label(ventana, text="Ingresa un dato:")
etiqueta.pack(padx=10, pady=10)

campo_texto = tk.Entry(ventana, width=30)
campo_texto.pack(padx=10, pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(padx=10, pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(padx=10, pady=5)

# Crear una lista para mostrar los datos
lista_datos = tk.Listbox(ventana, height=10, width=50)
lista_datos.pack(padx=10, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
