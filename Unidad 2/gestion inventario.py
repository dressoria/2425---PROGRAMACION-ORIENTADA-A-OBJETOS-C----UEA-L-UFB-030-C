class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if self.buscar_producto_por_id(producto.get_id()) is None:
            self.productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' agregado exitosamente.")
        else:
            print("El ID del producto ya existe. No se puede agregar.")

    def eliminar_producto(self, id_producto):
        producto = self.buscar_producto_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            print(f"Producto '{producto.get_nombre()}' eliminado exitosamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        producto = self.buscar_producto_por_id(id_producto)
        if producto:
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            print(f"Producto '{producto.get_nombre()}' actualizado exitosamente.")
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_id(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    def buscar_productos_por_nombre(self, nombre):
        productos_encontrados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        return productos_encontrados

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: ${producto.get_precio():.2f}")


def menu():
    inventario = Inventario()
    
    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                id_producto = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: $"))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Por favor, ingrese valores válidos.")

        elif opcion == '2':
            try:
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("Por favor, ingrese un ID válido.")

        elif opcion == '3':
            try:
                id_producto = int(input("Ingrese el ID del producto a actualizar: "))
                nueva_cantidad = input("Ingrese la nueva cantidad (deje vacío si no desea cambiarla): ")
                nuevo_precio = input("Ingrese el nuevo precio (deje vacío si no desea cambiarlo): ")
                
                if nueva_cantidad:
                    nueva_cantidad = int(nueva_cantidad)
                else:
                    nueva_cantidad = None
                
                if nuevo_precio:
                    nuevo_precio = float(nuevo_precio)
                else:
                    nuevo_precio = None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("Por favor, ingrese valores válidos.")

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            productos = inventario.buscar_productos_por_nombre(nombre)
            if productos:
                print(f"\nProductos encontrados con el nombre '{nombre}':")
                for producto in productos:
                    print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: ${producto.get_precio():.2f}")
            else:
                print(f"No se encontraron productos con el nombre '{nombre}'.")

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, por favor intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
