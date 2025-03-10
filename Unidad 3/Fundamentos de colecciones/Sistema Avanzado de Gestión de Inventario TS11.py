#GUARADAR EN UN ARCHIVO JSON
import json


# Clase producto
class Producto:
    def __init__(self,id_producto, nombre, cantidad, precio ):
        self.id_producto= id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_precio(self,precio_nuevo):
        self.precio = precio_nuevo


    def actualizar_cantidad(self,cantidad_nueva):
        self.cantidad = cantidad_nueva

    def to_dict(self):
        return {self.id_producto, self.nombre, self.cantidad, self.precio }

    def __str__(self):
        return f'id_producto:{self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}'


class Inventario:
    def __init__(self, archivo="inventario.json"):
            self.archivo = archivo
            self.productos = {}
            self.cargar_inventario()


    def cargar_inventario(self):
        try:
             with open(self.archivo, "r") as  f:
                  data = json.load(f)
                  self.productos = {int(k): Producto(**v) for k, v in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}

    def guardar_inventario(self):
        with open(self.archivo, 'w') as f:
            json.dumps({k: v.to_dict() for k, v in self.productos.items()}, f, indent=4)

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("ID inexistente.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()
            print("Exitosamente producto agg.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
                del self.productos[id_producto]
                self.guardar_inventario()
                print("Eliminado exitosa")

    def actualiar_precio(self, id_producto, precio_nuevo):
        if id_producto in self.productos:
                self.productos[id].actualizar_precio(precio_nuevo)
                self.guardar_inventario()
                print("actualizacion exitosa")
        else:
                print("Produto no encontrado")

    def actualizar_cantidad(self, id_producto, cantidad_nueva):
        if id_producto in self.productos:
                self.productos[id_producto].actualizar_cantidad(cantidad_nueva)
                self.guardar_inventario()
                print("actualizacion exitosa")
        else:
                print("Produto no encontrado")


#--


    def buscar_producto_nombre(self, nombre):
             resultado = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
             return resultado if resultado else "No se encontro el producto"


    def mostrar_inventario(self):
        if self.productos:
              for producto in self.productos.values():
                    print(producto)
        else:
               print("Producto no encontrado")

        # Interfaz de usuario en la consola
def menu():
   inventario = Inventario()
   while True:
        print("\n-- Gestion de intentario--")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6.1  Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":  # Agregar producto
            id_producto= input("ingrese id del producto: ")
            nombre = input("INDRESE Nombre del producto: ")
            cantidad = int(input("INGRESE cantidad: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            print("producto agg correctamente")



        elif opcion == "2":  # Eliminar producto
            id_producto = int(input("ingrese id del producto: "))
            inventario.eliminar_producto(id_producto)
            print("Producto eliminado")


        elif opcion == "3":  # Actualizar producto
            print("\nActualizar ")
            id_producto = int(input('Ingresar ID del producto de actualizar: '))
            precio = float(input("Ingresar precio del producto: "))
            inventario.actualizar_precio(id_producto, precio)
            print("Precio actualizado")


        elif opcion == "4":  # Buscar producto
            print("\nBuscar Producto")
            nombre = input("Ingresar nombre del producto: ")
            producto = inventario.buscar_producto(nombre)
            print("Nombre a encontrar")
            print(producto.id_producto , producto.nombre, producto.precio)


        elif opcion == '5':# Mostrar inventario
            print("\nMostrar Inventario")
            inventario.mostrar_inventario()

        elif opcion == '6':  # Mostrar inventario
           print("Saliendo del Inventario")
           break

        else:
            print("opcion no validad")

if __name__ == "__main__":
    menu()