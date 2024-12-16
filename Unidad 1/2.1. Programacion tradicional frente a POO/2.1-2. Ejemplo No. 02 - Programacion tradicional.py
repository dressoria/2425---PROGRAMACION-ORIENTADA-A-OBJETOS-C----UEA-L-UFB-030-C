# Programación Tradicional
# Ejemplo: Gestión de un automóvil

# Definición de variables globales
tanque_combustible = 0
kilometraje = 0
eficiencia_combustible = 25

# Función para llenar el tanque de combustible
def llenar_tanque(cantidad):
    global tanque_combustible
    tanque_combustible += cantidad

# Función para conducir el automóvil
def conducir(distancia):
    global tanque_combustible, kilometraje, eficiencia_combustible
    combustible_necesario = distancia / eficiencia_combustible
    if combustible_necesario <= tanque_combustible:
        tanque_combustible -= combustible_necesario
        kilometraje += distancia
        print("Conduciendo:", distancia, "kilómetros")
    else:
        print("No hay suficiente combustible para esa distancia.")

# Uso de las funciones en la programación tradicional
llenar_tanque(20)
conducir(100)

# Imprimir el kilometraje y el nivel de combustible restante
print("Kilometraje (Tradicional):", kilometraje)
print("Tanque de combustible (Tradicional):", tanque_combustible)
