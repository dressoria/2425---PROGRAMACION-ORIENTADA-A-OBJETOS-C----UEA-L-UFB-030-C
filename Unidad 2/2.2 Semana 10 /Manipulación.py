import os

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde el archivo, si existe."""
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    producto, cantidad = linea.strip().split(",")
                    self.productos[producto] = int(cantidad)
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no existe. Se creará uno nuevo.")
        except PermissionError:
            print(f"No tienes permiso para leer el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda el inventario en el archivo."""
        try:
            with open(self.archivo, "w") as file:
                for producto, cantidad in self.productos.items():
                    file.write(f"{producto},{cantidad}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print(f"No tienes permiso para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto, cantidad):
        """Añade un producto o actualiza su cantidad."""
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad
        self.guardar_inventario()
        print(f"Producto '{producto}' añadido/actualizado exitosamente.")

    def eliminar_producto(self, producto):
        """Elimina un producto del inventario."""
        if producto in self.productos:
            del self.productos[producto]
            self.guardar_inventario()
            print(f"Producto '{producto}' eliminado exitosamente.")
        else:
            print(f"El producto '{producto}' no se encuentra en el inventario.")

    def actualizar_producto(self, producto, cantidad):
        """Actualiza la cantidad de un producto."""
        if producto in self.productos:
            self.productos[producto] = cantidad
            self.guardar_inventario()
            print(f"Producto '{producto}' actualizado exitosamente.")
        else:
            print(f"El producto '{producto}' no existe en el inventario.")

    def mostrar_inventario(self):
        """Muestra el inventario actual."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for producto, cantidad in self.productos.items():
                print(f"{producto}: {cantidad}")

# Función principal para interactuar con el sistema de inventario
def menu():
    inventario = Inventario()

    while True:
        print("\nMenú de Gestión de Inventario:")
        print("1. Mostrar inventario")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Actualizar producto")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            inventario.mostrar_inventario()
        elif opcion == "2":
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            inventario.agregar_producto(producto, cantidad)
        elif opcion == "3":
            producto = input("Ingrese el nombre del producto a eliminar: ")
            inventario.eliminar_producto(producto)
        elif opcion == "4":
            producto = input("Ingrese el nombre del producto a actualizar: ")
            cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario.actualizar_producto(producto, cantidad)
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu()
