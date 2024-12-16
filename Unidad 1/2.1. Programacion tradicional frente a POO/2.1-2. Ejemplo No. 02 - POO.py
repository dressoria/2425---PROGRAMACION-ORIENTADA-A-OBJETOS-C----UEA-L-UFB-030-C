# Programación Orientada a Objetos (POO)
# Ejemplo: Gestión de un automóvil

class Automovil:
    def __init__(self, eficiencia_combustible=25):
        self.tanque_combustible = 0
        self.kilometraje = 0
        self.eficiencia_combustible = eficiencia_combustible

    def llenar_tanque(self, cantidad):
        self.tanque_combustible += cantidad

    def conducir(self, distancia):
        combustible_necesario = distancia / self.eficiencia_combustible
        if combustible_necesario <= self.tanque_combustible:
            self.tanque_combustible -= combustible_necesario
            self.kilometraje += distancia
            print("Conduciendo:", distancia, "kilómetros")
        else:
            print("No hay suficiente combustible para esa distancia.")

# Crear una instancia de la clase Automovil
auto = Automovil()

# Uso de los métodos en la programación orientada a objetos
auto.llenar_tanque(20)
auto.conducir(100)

# Imprimir el kilometraje y el nivel de combustible restante
print("Kilometraje (POO):", auto.kilometraje)
print("Tanque de combustible (POO):", auto.tanque_combustible)
