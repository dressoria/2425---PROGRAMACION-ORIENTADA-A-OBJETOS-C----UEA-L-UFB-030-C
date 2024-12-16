class Combatiente:

    def __init__(self, alias, fuerza, sabiduría, resistencia, salud):
        self.alias = alias
        self.fuerza = fuerza
        self.sabiduría = sabiduría
        self.resistencia = resistencia
        self.salud = salud

    def mostrar_atributos(self):
        print(self.alias, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Sabiduría:", self.sabiduría)
        print("·Resistencia:", self.resistencia)
        print("·Salud:", self.salud)

    def mejorar(self, fuerza, sabiduría, resistencia):
        self.fuerza += fuerza
        self.sabiduría += sabiduría
        self.resistencia += resistencia

    def vivo(self):
        return self.salud > 0

    def caer(self):
        self.salud = 0
        print(self.alias, "ha caído")

    def calcular_ataque(self, oponente):
        return self.fuerza - oponente.resistencia

    def golpear(self, oponente):
        daño = self.calcular_ataque(oponente)
        oponente.salud -= daño
        print(self.alias, "causa", daño, "de daño a", oponente.alias)
        if oponente.vivo():
            print("Salud de", oponente.alias, "es", oponente.salud)
        else:
            oponente.caer()


class Luchador(Combatiente):

    def __init__(self, alias, fuerza, sabiduría, resistencia, salud, espada):
        super().__init__(alias, fuerza, sabiduría, resistencia, salud)
        self.espada = espada

    def cambiar_arma(self):
        opción = int(input("Elige una espada: (1) Acero del Rey, daño 8. (2) Espada del Dragón, daño 10"))
        if opción == 1:
            self.espada = 8
        elif opción == 2:
            self.espada = 10
        else:
            print("Opción de arma inválida")

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print("·Espada:", self.espada)

    def calcular_ataque(self, oponente):
        return self.fuerza * self.espada - oponente.resistencia


class Hechicero(Combatiente):

    def __init__(self, alias, fuerza, sabiduría, resistencia, salud, grimorio):
        super().__init__(alias, fuerza, sabiduría, resistencia, salud)
        self.grimorio = grimorio

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print("·Grimorio:", self.grimorio)

    def calcular_ataque(self, oponente):
        return self.sabiduría * self.grimorio - oponente.resistencia


def enfrentamiento(combatiente_1, combatiente_2):
    turno = 0
    while combatiente_1.vivo() and combatiente_2.vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", combatiente_1.alias, ":", sep="")
        combatiente_1.golpear(combatiente_2)
        print(">>> Acción de ", combatiente_2.alias, ":", sep="")
        combatiente_2.golpear(combatiente_1)
        turno += 1
    if combatiente_1.vivo():
        print("\nHa ganado", combatiente_1.alias)
    elif combatiente_2.vivo():
        print("\nHa ganado", combatiente_2.alias)
    else:
        print("\nEmpate")


guerrero_1 = Luchador("Alduin", 18, 8, 6, 120, 5)
mago_1 = Hechicero("Merlina", 6, 18, 5, 110, 4)

guerrero_1.mostrar_atributos()
mago_1.mostrar_atributos()

enfrentamiento(guerrero_1, mago_1)
