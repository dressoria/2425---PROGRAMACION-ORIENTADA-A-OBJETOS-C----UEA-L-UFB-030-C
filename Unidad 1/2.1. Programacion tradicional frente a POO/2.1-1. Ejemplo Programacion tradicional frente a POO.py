# Programación Tradicional
# Ejemplo: Gestión de una cuenta financiera

# Definición de variables globales
saldo = 0
tasa_interes = 0.05

# Función para ingresar dinero en la cuenta
def ingresar(dinero):
    global saldo
    saldo += dinero

# Función para retirar dinero de la cuenta
def retirar(dinero):
    global saldo
    saldo -= dinero

# Función para calcular el interés y actualizar el saldo
def calcular_intereses():
    global saldo, tasa_interes
    intereses = saldo * tasa_interes
    saldo += intereses

# Uso de las funciones en la programación tradicional
ingresar(1000)
retirar(500)
calcular_intereses()

# Imprimir el saldo final
print("Saldo (Tradicional):", saldo)


# Programación Orientada a Objetos (POO)
# Ejemplo: Gestión de una cuenta financiera

class CuentaFinanciera:
    def __init__(self, saldo_inicial=0, tasa_interes=0.05):
        self.saldo = saldo_inicial
        self.tasa_interes = tasa_interes

    def ingresar(self, dinero):
        self.saldo += dinero

    def retirar(self, dinero):
        self.saldo -= dinero

    def calcular_intereses(self):
        intereses = self.saldo * self.tasa_interes
        self.saldo += intereses

# Crear una instancia de la clase CuentaFinanciera
cuenta = CuentaFinanciera()

# Uso de los métodos en la programación orientada a objetos
cuenta.ingresar(1000)
cuenta.retirar(500)
cuenta.calcular_intereses()

# Imprimir el saldo final
print("Saldo (POO):", cuenta.saldo)
