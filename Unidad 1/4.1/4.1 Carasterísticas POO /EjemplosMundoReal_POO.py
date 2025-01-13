# Aqui definimoslaclase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

# Aqui mostramos la Definición de la clase Cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []
    
    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)
    
    def ver_carrito(self):
        if not self.carrito:
            print("El carrito está vacío.")
        else:
            for producto in self.carrito:
                print(producto)

    def total_carrito(self):
        total = sum([producto.precio for producto in self.carrito])
        return total

# Ponemos la definición de la clase Tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

# ponemos el Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear productos
    p1 = Producto("Camiseta", 20)
    p2 = Producto("Pantalón", 40)
    
    # Crear tienda
    tienda = Tienda("Mi Tienda Online")
    tienda.agregar_producto(p1)
    tienda.agregar_producto(p2)
    
    # Mostrar productos en la tienda
    print("Productos en la tienda:")
    tienda.mostrar_productos()
    
    # Crear cliente
    cliente = Cliente("Juan")
    
    # El cliente agrega productos al carrito
    cliente.agregar_al_carrito(p1)
    cliente.agregar_al_carrito(p2)
    
    # Mostrar carrito del cliente
    print("\nCarrito de compras de", cliente.nombre + ":")
    cliente.ver_carrito()
    
    # Mostrar el total del carrito
    print(f"\nTotal del carrito: ${cliente.total_carrito()}")
