#EJEMPLO COMPUTO,CLIENTE,CYBER
from tkinter.constants import SEL_LAST


class Computo:
    def __init__(self, marca,tiempo):
        self.marca = marca
        self.tiempo = tiempo
        self.is_rented = False

    def rent(self):
        """Rentar el computo si no esta en uso."""
        if not self.is_rented:
            self.is_rented = True
            return True
        return False

    def NOpago_tiempo(self):
        """Se realizar el pago"""
        self.is_rented = True

    def __str__(self):
        return f"El computo de marca {self.marca} se rento por{self.tiempo} minutos"

class Cyber:
    """"""
    def __init__(self, administrador):
        self.administrador = administrador

    def alquiler_computo(self, computo, action):
        """Se renta o se paga  computo dependiendo de su disponibilidad"""
        if action == 'rent':
            return computo.rent()
        elif action == 'ya esta rentado':
            computo.NOpago_tiempo()

class Cliente:
    """EL CLIENTE ES EL QUE VA ALQUILAR LOS COMPUTOS"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.rented_computs = []

    def rent_computo(self, computo, cyber):
        if cyber.alquiler_computo(computo, 'rent'):
            self.rented_computs.append(computo)
            print(f"{self.name} a rentado el computo {computo.marca}")
        else:
            print(f" El computo {computo.marca} no esta disponible")

    def NOpago_tiempo(self, computo, cyber):
        """no estuvo disponible un computo"""
        if computo in self.rented_computs:
            cyber.alquiler_computo(computo, "No pago")
            self.rented_computs.remove(computo)

#CREAR OBJETOS,PERSONA(COMPUTO,USUARIO)
escritorio = Computo('HP',"30M")
administrador = Cyber('Felipe')
user = Cliente('Junior', '17')

user.rent_computo(escritorio, administrador)