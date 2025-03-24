import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry  # Importo la librería para el selector de fechas

class AgendaApp:
    def __init__(self, root):
        # Yo aquí creo la ventana principal
        self.root = root
        self.root.title("Agenda Personal")

        # Yo aquí creo los Frames para organizar mejor los componentes
        self.frame_eventos = tk.Frame(self.root)
        self.frame_eventos.pack(pady=10)
        
        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10)
        
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        # Yo aquí creo la Treeview para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Yo aquí agrego los campos de entrada para la fecha, hora y descripción
        self.label_fecha = tk.Label(self.frame_entrada, text="Fecha:")
        self.label_fecha.grid(row=0, column=0, padx=5)

        self.date_entry = DateEntry(self.frame_entrada, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5)

        self.label_hora = tk.Label(self.frame_entrada, text="Hora:")
        self.label_hora.grid(row=1, column=0, padx=5)

        self.entry_hora = tk.Entry(self.frame_entrada)
        self.entry_hora.grid(row=1, column=1, padx=5)

        self.label_desc = tk.Label(self.frame_entrada, text="Descripción:")
        self.label_desc.grid(row=2, column=0, padx=5)

        self.entry_desc = tk.Entry(self.frame_entrada)
        self.entry_desc.grid(row=2, column=1, padx=5)

        # Yo aquí creo los botones para agregar y eliminar eventos
        self.boton_agregar = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.boton_agregar.grid(row=0, column=0, padx=5)

        self.boton_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.boton_eliminar.grid(row=0, column=1, padx=5)

        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=self.salir)
        self.boton_salir.grid(row=0, column=2, padx=5)

    def agregar_evento(self):
        fecha = self.date_entry.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_desc.get()

        if not fecha or not hora or not descripcion:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Agrego el evento a la Treeview
        self.tree.insert("", "end", values=(fecha, hora, descripcion))

    def eliminar_evento(self):
        try:
            # Elimino el evento seleccionado en la Treeview
            selected_item = self.tree.selection()[0]
            self.tree.delete(selected_item)
        except IndexError:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ningún evento.")

    def salir(self):
        # Cierro la aplicación
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
