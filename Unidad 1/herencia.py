# Miherencia

class Pokemon:

    def __init__(self, nombre, color, peso):
        self.nombre = nombre
        self.color = color
        self.peso = peso

    def eat(self):
        self.peso = + 1

class electrico(Pokemon):
    def __init__(self, nombre, color, peso, nivel):
        super().__init__(nombre, color, peso)
        self.nivel = nivel

class tierra(Pokemon):
    def __init__(self, nombre, color, peso,  nivel):
        super().__init__(nombre, color, peso)
        self.nivel = nivel

mi_electrico = electrico("pikachu", 'amarrillo', '97', '33')
mi_tierra = tierra('golem', 'cafe', '97', '89')

#PRIN_POKEMON
print(mi_electrico.nombre, mi_electrico.color, mi_electrico.peso, mi_electrico.nivel)
print(mi_tierra.nombre, mi_tierra.color, mi_tierra.peso, mi_tierra.nivel)