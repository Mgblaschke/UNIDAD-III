class Coche:
    #MI CONSTRUCTOR
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

#INSTANCIAR UN OBJETO
automobil = Coche('azul', 'toyota', '2018')
tesla = Coche('blanco', 'tesla', 'modelo 2')

print(type(automobil))
print(type(tesla))

print(automobil.color, automobil.modelo, automobil.marca)
print(tesla.color, tesla.modelo, tesla.marca)
#USO DE LOS METODOS
automobil.arrancar()
tesla.arrancar()
#IMPRIMO
print(automobil.arrancado)
print(tesla.arrancado)

automobil.parar()
tesla.parar()