#Polimorfismo
#diferentes clases tengan el mismo metodo , pero comportamientos diferentes

class Pokemon:
    def __init__(self, nombre, color, peso):
        self.nombre = nombre
        self.color = color
        self.peso = peso


    def attack_type(self):
#metodo generico
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

# clase hija
class electrico(Pokemon):
    def __init__(self, nombre, color, peso, attack):
          super().__init__(nombre, color, peso)
          self.attack = attack
#VA SOBREESCRIBIR
    def attack_type(self):
      return f"{self.nombre} {self.color} {self.peso} {self.attack} su attack :  IMPACTRUENO"

class tierra(Pokemon):
    def __init__(self, nombre, color, peso,  pv):
        super().__init__(nombre, color, peso)
        self.pv = pv

    def attack_type(self):
       return f"{self.nombre} {self.color} {self.peso} {self.pv} su attack : TERREMOTO"

#FUNCIOM PARA APLICAR POLIMORFISMO

def mostrar_attack_type(pokemon):
    print(pokemon.attack_type())

#CREAR MI OBJETO
mi_pokemon = electrico('Pikachu', 'amarillo', '97', 'IMPACTRUENO')

#USO DEL POLIMORFISMO
mostrar_attack_type(mi_pokemon)
