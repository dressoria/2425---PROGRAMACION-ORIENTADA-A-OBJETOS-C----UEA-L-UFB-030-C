import tkinter as tk
from tkinter import messagebox

# Función para agregar una tarea
def agregar_tarea():
    tarea = entry_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entry_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

# Función para marcar una tarea como completada
def marcar_completada(event):
    try:
        tarea_seleccionada = lista_tareas.curselection()
        if tarea_seleccionada:
            tarea = lista_tareas.get(tarea_seleccionada)
            tarea_completada = f"{tarea} (Completada)"
            lista_tareas.delete(tarea_seleccionada)
            lista_tareas.insert(tk.END, tarea_completada)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")
    except Exception as e:
        print(e)

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()
        if tarea_seleccionada:
            lista_tareas.delete(tarea_seleccionada)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")
    except Exception as e:
        print(e)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas Mejorada")

# Crear un campo de entrada para nuevas tareas
entry_tarea = tk.Entry(ventana, width=40)
entry_tarea.pack(pady=10)

# Crear botón para añadir tarea
boton_añadir = tk.Button(ventana, text="Añadir Tarea", width=20, command=agregar_tarea)
boton_añadir.pack(pady=5)

# Crear lista de tareas con un estilo visual mejorado
lista_tareas = tk.Listbox(ventana, height=10, width=50, selectmode=tk.SINGLE, bg="#f0f0f0", font=("Arial", 12))
lista_tareas.pack(pady=10)

# Crear botones para marcar como completada y eliminar tareas
boton_completar = tk.Button(ventana, text="Marcar como Completada", width=20, command=marcar_completada)
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", width=20, command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Vincular la tecla Enter para agregar tareas
ventana.bind('<Return>', lambda event: agregar_tarea())

# Vincular el doble clic para marcar una tarea como completada
lista_tareas.bind("<Double-1>", marcar_completada)

# Ejecutar la aplicación
ventana.mainloop()
