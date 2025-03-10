# Versión 1 - Implementación de la biblioteca digital

# Empezamos creando la clase Libro, que tendrá atributos como título, autor, categoría y ISBN.
# Utilizamos una tupla para título y autor porque esos valores no cambiarán una vez asignados.
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # La tupla asegura que el título y autor sean inmutables.
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
    
    def __repr__(self):
        return f"Libro({self.titulo}, {self.autor}, {self.categoria}, {self.isbn})"


# Ahora creamos la clase Usuario, con un ID único, nombre y lista de libros prestados.
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []
    
    def __repr__(self):
        return f"Usuario({self.nombre}, {self.user_id})"


# La clase Biblioteca será la encargada de gestionar los libros, usuarios y los préstamos.
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros por ISBN
        self.usuarios = set()  # Conjunto para asegurar IDs de usuario únicos
    
    def anadir_libro(self, libro):
        # Añadir un libro al sistema utilizando el ISBN como clave.
        self.libros[libro.isbn] = libro
        print(f"Libro '{libro.titulo}' añadido a la biblioteca.")
    
    def quitar_libro(self, isbn):
        # Eliminar un libro usando su ISBN.
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no existe en la biblioteca.")
    
    def registrar_usuario(self, usuario):
        # Añadir un usuario asegurando que su ID es único.
        if usuario.user_id not in {u.user_id for u in self.usuarios}:
            self.usuarios.add(usuario)
            print(f"Usuario '{usuario.nombre}' registrado.")
        else:
            print("Este ID de usuario ya está registrado.")
    
    def dar_de_baja_usuario(self, user_id):
        # Dar de baja un usuario usando su ID.
        usuario_a_baja = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario_a_baja:
            self.usuarios.remove(usuario_a_baja)
            print(f"Usuario con ID {user_id} dado de baja.")
        else:
            print("Usuario no encontrado.")
    
    def prestar_libro(self, isbn, user_id):
        # Prestar un libro a un usuario.
        if isbn in self.libros:
            libro = self.libros[isbn]
            usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
            if usuario:
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")
            else:
                print("Usuario no encontrado.")
        else:
            print("El libro no está disponible.")
    
    def devolver_libro(self, isbn, user_id):
        # Devolver un libro prestado por un usuario.
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario:
            libro_a_devolver = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
            if libro_a_devolver:
                usuario.libros_prestados.remove(libro_a_devolver)
                print(f"Libro '{libro_a_devolver.titulo}' devuelto por '{usuario.nombre}'.")
            else:
                print("El libro no está prestado a este usuario.")
        else:
            print("Usuario no encontrado.")
    
    def buscar_libro(self, criterio):
        # Buscar un libro por título, autor o categoría.
        libros_encontrados = [libro for libro in self.libros.values() if (criterio.lower() in libro.titulo.lower() or 
                                                                          criterio.lower() in libro.autor.lower() or 
                                                                          criterio.lower() in libro.categoria.lower())]
        return libros_encontrados
    
    def listar_libros_prestados(self, user_id):
        # Listar los libros prestados a un usuario.
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario:
            return usuario.libros_prestados
        else:
            print("Usuario no encontrado.")
            return []

# Ejemplo de uso
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "12345")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "67890")

# Crear usuarios
usuario1 = Usuario("Juan Pérez", 1)
usuario2 = Usuario("María Gómez", 2)

# Registrar usuarios y añadir libros
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)
biblioteca.anadir_libro(libro1)
biblioteca.anadir_libro(libro2)

# Prestar libros
biblioteca.prestar_libro("12345", 1)

# Buscar libro
resultados = biblioteca.buscar_libro("Cien")
print("Libros encontrados:", resultados)

# Devolver libro
biblioteca.devolver_libro("12345", 1)
