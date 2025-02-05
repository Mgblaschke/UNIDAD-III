#En este codigo aplicaremos los conocimientos adquiridos sobre Definición de Clase, Definición de Objeto, Herencia, Encapsulación y Polimorfismo
#Damos incio a nustra clase y sus atributos

class Digimon:
    def __init__(self, nombre, color, salud):
        self.nombre = nombre
        self.color = color
        self.__salud = salud #salud sera un el atributo protegido

    def obtener_salud(self): #nos permite acceder al atributo portejido
        return self.__salud

    def valores(self):
        return f" Su nombre es {self.nombre} de color {self.color} salud aprox. de {self.__salud}"


class Pasivo(Digimon):
    def __init__(self, nombre, color, salud, tipohielo):
        super().__init__(nombre, color, salud)
        self.tipohielo = tipohielo

    def valores(self):
        return f" Su nombre es {self.nombre} de color observado {self.color} salud {self.obtener_salud()} tipohielo {self.tipohielo}"

def mostrar_valores(digimon):
    print(digimon.valores())




#instanciamos
digimon1 = Digimon('totoi','amarillo','50S')
pasivo1 = Pasivo('lapras','plomo', '150S', 'si')
print(digimon1.nombre)
print(digimon1.color)
print(digimon1.obtener_salud())#resultado del encapsulacion elaborada
#resultado del polimorfismo
mostrar_valores(digimon1)
mostrar_valores(pasivo1)