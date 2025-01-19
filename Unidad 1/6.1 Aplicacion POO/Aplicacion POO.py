# Clase base
class Animal:
    def __init__(self, nombre, edad):
        # Aquí definimos un atributo público 'nombre' para que sea accesible desde fuera de la clase
        self.nombre = nombre  
        # En este caso, uso un atributo privado '__edad' para aplicar el concepto de encapsulación
        self.__edad = edad    
    
    # Aquí defino un método 'hablar' en la clase base, que puede ser sobrescrito en las clases hijas
    def hablar(self):
        return f"{self.nombre} hace un sonido."

    # Usamos un getter para acceder al atributo privado '__edad'. Este es un ejemplo de encapsulación
    def get_edad(self):
        return self.__edad

    # Usamos un setter para modificar el valor de '__edad'. Esto también es parte de la encapsulación.
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad no válida.")

# Clase derivada (hereda de Animal)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamo al constructor de la clase base usando 'super()', para asegurarme de que los atributos base se inicialicen correctamente
        super().__init__(nombre, edad)  
        # Aquí añado un nuevo atributo específico de la clase 'Perro'
        self.raza = raza

    # Sobrescribo el método 'hablar' para darle un comportamiento específico para los perros
    def hablar(self):
        return f"{self.nombre} dice ¡Guau!"

# Clase derivada (hereda de Animal)
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        # Al igual que en la clase 'Perro', llamo al constructor de la clase base para inicializar los atributos heredados
        super().__init__(nombre, edad)  
        # Aquí añado un atributo específico de la clase 'Gato'
        self.color = color

    # Sobrescribo el método 'hablar' para darle un comportamiento específico para los gatos
    def hablar(self):
        return f"{self.nombre} dice ¡Miau!"

# Polimorfismo: La función 'hacer_sonar' usa un solo método (hablar), pero puede ejecutar diferentes versiones del método
def hacer_sonar(animal):
    # Aquí llamo al método 'hablar' del objeto, y dependiendo de la clase del objeto, se ejecutará una versión distinta del método
    print(animal.hablar())

# Crear instancias de las clases
perro = Perro("Rex", 5, "Labrador")
gato = Gato("Whiskers", 3, "Gris")

# Acceder a los atributos públicos y privados. Aquí mostramos cómo trabajar con encapsulación.
print(f"{perro.nombre} tiene {perro.get_edad()} años.")
perro.set_edad(6)  # Modifico la edad del perro usando el setter
print(f"Ahora, {perro.nombre} tiene {perro.get_edad()} años.")

# Usamos la función 'hacer_sonar' para demostrar polimorfismo
hacer_sonar(perro)  # En este caso, 'Rex' dice ¡Guau!
hacer_sonar(gato)   # En este caso, 'Whiskers' dice ¡Miau!
