# Programación Orientada a Objetos (POO)
# Ejemplo: descripcion y procedimiento de un coche
class Coche:
    def __init__(self, color, marca, modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False

    def arrancar(self):
        self.arrancado =  True
        print('El', self.color, self.marca, self.modelo, 'se ha arrancado')

    def parar(self):
        self.arrancado =  False
        print('El', self.color, self.marca, self.modelo, 'se ha parado')

#CREAR UNA INSTANCIA DE UN COCHE
automobil = Coche('azul', 'toyota', '2018')
tesla = Coche('blanco', 'tesla', 'modelo 2')

print(type(automobil))
print(type(tesla))

print(automobil.color, automobil.modelo, automobil.marca)
print(tesla.color, tesla.modelo, tesla.marca)
#USO DE LOS METODOS EN POO
automobil.arrancar()
tesla.arrancar()
#IMPRIMIR EL ARRANCADO Y PARAR DEL COCHE
print(automobil.arrancado)
print(tesla.arrancado)

automobil.parar()
tesla.parar()