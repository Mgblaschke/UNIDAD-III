# ENCAPSULAMIENTO
#DUELOS 1VS1 PROTEGER EL TURNO ENTRE ATAQUES
class Pelea_pokemon:
    def __init__(self, atacar):
        self.__turno = atacar

    def recibir(self, ataque):
        self.__turno +=ataque #PARA ACCEDER A MI TURNO DEBO RECIBIR UN ATAQUE

    def curarme(self, ataque):
        self.__turno +=ataque

    def obtener_turno(self):
        return self.__turno

# creo instancia
mi_pelea = Pelea_pokemon(8)
print(mi_pelea.obtener_turno())

mi_pelea.recibir(3)
print(mi_pelea.obtener_turno())