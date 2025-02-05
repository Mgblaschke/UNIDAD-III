#Ejemplo del metodo contructor
#Creamos la clase lapto
class Lapto:
    def __init__(self, marca, procesador, precio):
        self.marca = marca
        self.procesador = procesador
        self.precio = precio

#Uso del destructor
    def __del__(self):
        print(f"actualizacion de precio.")

#resultado al instanciar de la clase Lapto
mi_lapto = Lapto('HP', 'intel', '$299')
print(mi_lapto.marca)
print(mi_lapto.procesador)
print(mi_lapto.precio)
#Aplicacion del metodo destructor
del mi_lapto