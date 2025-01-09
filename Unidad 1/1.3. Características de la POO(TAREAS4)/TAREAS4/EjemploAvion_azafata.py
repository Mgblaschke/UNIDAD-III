#AVION CON NOVATA
class Avion:
    def __init__(self, capacidad, longitud, envergadura):
        self.capacidad = capacidad
        self.longitud = longitud
        self.envergadura = envergadura
        self.azafata = None

#ASIGNAREMOS UNA AZAFATA
    def asignar_azafata(self, novata):
        if isinstance(novata, novata):
            self.azafata = novata

    def __str__(self):
        return  f'El Avion tiene una capacidad de {self.capacidad} personas, cuenta con una longitud de {self.longitud} y {self.envergadura} de envergadura.'

class novata:
    def __init__(self,nombre, carnet):
        self.nombre = nombre
        self.carnet = carnet

    def __str__(self):
        return f'Novata llamada {self.nombre} resivio su {self.carnet} para su primer vuelo como azafata.'
#CREACION DE OBJETOS
avioneconomico = Avion('120', '50m', '43m')
avionelite = Avion('320', '73M', '56M')
azafata = novata('jessica', 'elite')

#ASIGNACION DE AZAFATA
avionelite.asignar_azafata(novata)
#IMPRIMIMOS
print(avionelite)
print(azafata)