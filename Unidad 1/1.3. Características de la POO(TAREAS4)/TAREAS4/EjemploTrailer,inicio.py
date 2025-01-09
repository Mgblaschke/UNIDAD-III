#CLASE TRAILER

class Trailer:
    def __init__(self,modelo, anio, altura):
        self.modelo = modelo
        self.anio = anio
        self.altura = altura
        self.velocidad = 0

    def arrancamos(self, acelerar):
        self.velocidad += acelerar
        print(f' Mi trailer del {self.anio} de modelo {self.modelo} arranco a una velocidad de {self.velocidad}')

    def parar(self, reduccion):
        self.velocidad -= reduccion
        print(f' Mi trailer del {self.anio} de modelo {self.modelo} paro a una velocidad {self.velocidad}')

#CREACCION DE OBJETOS
Mi_trailer = Trailer('Americano', "89", "5m")
Mi_trailer.arrancamos(20)
Mi_trailer.parar(10)
print(f'la velocidad de mi trailer termino en : {Mi_trailer.velocidad}')