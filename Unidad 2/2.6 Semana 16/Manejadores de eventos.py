import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Crear la lista de tareas
tasks = []

# Función para agregar una nueva tarea
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_task_list()
        entry.delete(0, tk.END)

# Función para eliminar la tarea seleccionada
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        del tasks[selected_task_index]
        update_task_list()
    except IndexError:
        messagebox.showwarning("Seleccionar tarea", "No has seleccionado ninguna tarea.")

# Función para marcar una tarea como completada
def complete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks[selected_task_index] = f"{tasks[selected_task_index]} (Completada)"
        update_task_list()
    except IndexError:
        messagebox.showwarning("Seleccionar tarea", "No has seleccionado ninguna tarea.")

# Función para actualizar la lista de tareas en el Listbox
def update_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Función para cerrar la aplicación
def close_app(event=None):
    root.quit()

# Crear la entrada de texto para agregar nuevas tareas
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Botón para agregar una tarea
add_button = tk.Button(root, text="Añadir tarea", command=add_task)
add_button.pack(pady=5)

# Crear la lista de tareas
listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Botón para eliminar la tarea seleccionada
delete_button = tk.Button(root, text="Eliminar tarea", command=delete_task)
delete_button.pack(pady=5)

# Botón para marcar la tarea seleccionada como completada
complete_button = tk.Button(root, text="Marcar como completada", command=complete_task)
complete_button.pack(pady=5)

# Asignar atajos de teclado
root.bind("<Return>", lambda event: add_task())  # Añadir tarea con "Enter"
root.bind("<Delete>", lambda event: delete_task())  # Eliminar tarea con "Delete"
root.bind("<c>", lambda event: complete_task())  # Marcar como completada con "C"
root.bind("<Escape>", lambda event: close_app())  # Cerrar aplicación con "Escape"

# Iniciar el loop de la interfaz
root.mainloop()
