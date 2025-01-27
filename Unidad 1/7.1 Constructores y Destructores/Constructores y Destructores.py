class Libro:
    # Constructor de la clase Libro
    def __init__(self, titulo, autor):
        # Aquí inicializo los atributos del libro
        self.titulo = titulo
        self.autor = autor
        print(f"El libro '{self.titulo}' de {self.autor} ha sido creado.")
    
    # Destructor de la clase Libro
    def __del__(self):
        # En este método se realiza la limpieza antes de que el objeto sea destruido
        print(f"El libro '{self.titulo}' de {self.autor} ha sido eliminado.")
    
    # Método para mostrar información del libro
    def mostrar_info(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}")

# Aquí empiezo a crear los objetos de la clase Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("La casa de los espíritus", "Isabel Allende")

# Uso del método para mostrar la información de los libros
libro1.mostrar_info()
libro2.mostrar_info()

# Aquí ya dejo que los objetos sean eliminados, para que el destructor sea llamado automáticamente
del libro1
del libro2
