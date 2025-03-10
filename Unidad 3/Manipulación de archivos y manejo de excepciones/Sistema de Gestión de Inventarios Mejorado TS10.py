#Clase producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"({self.id_producto}, {self.nombre}, {self.cantidad}, {self.precio})"

class Inventario:
    def __init__(self):
        self.productos = []

 #Open archivo lectura posterior de su elaboracion Datos_inventario.txt
    def repositorio_inventario(self):
        with open('Datos_inventario.txt',"r" ) as file:
            for line in file:
                nombre,cantidad,precio = line.strip()
                self.productos.append(Producto('id_producto','nombre','cantidad',float('precio')))


#GUARDAR la informacion de nuestro inventario en archivo txt
    def guardar_inventario(self):
        with open('Datos_inventario.txt',"w") as file:
            for producto in self.productos:
                file.write(f"{producto.id_producto} {producto.nombre} {producto.cantidad} {producto.precio}")


#AGG PRODUCTO
    def agregar_producto(self, producto):
            self.productos.append(producto)
            self.guardar_inventario()
            print('Producto agg correctamente')

#DEL PRODUCTO
    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                print("Producto eliminado")

#ACTUALIZACION DEL PRODUCTO
    def actualizar_precio(self, id_producto, precio):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                producto.precio = precio
                print('actualizacion exitosa')


    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto

    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto)


# Interfaz de usuario en la consola
def menu():
   mi_inventario = Inventario()
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
            cantidad = int(input("INGRESE cantidad producto: "))
            precio = float("Ingrese precio del producto: ")
            producto = Producto(id_producto, nombre, cantidad, precio)
            mi_inventario.agregar_producto(producto)
            print("producto agg correctamente")



        elif opcion == "2":  # Eliminar producto
            id_producto = int(input("ingrese id del producto: "))
            mi_inventario.eliminar_producto(id_producto)
            print("Producto eliminado")


        elif opcion == "3":  # Actualizar producto
            print("\nActualizar ")
            id_producto = int(input('Ingresar ID del producto de actualizar: '))
            precio = float(input("Ingresar precio del producto: "))
            mi_inventario.actualizar_precio(id_producto, precio)
            print("Precio actualizado")


        elif opcion == "4":  # Buscar producto
            print("\nBuscar Producto")
            nombre = input("Ingresar nombre del producto: ")
            producto = mi_inventario.buscar_producto(nombre)
            print("Nombre a encontrar")
            print(producto.id_producto , producto.nombre, producto.precio)


        elif opcion == '5':# Mostrar inventario
            print("\nMostrar Inventario")
            mi_inventario.mostrar_inventario()

        elif opcion == '6':  # Mostrar inventario
           print("Saliendo del Inventario")
           break

        else:
            print("opcion no validad")

if __name__ == "__main__":
    menu()
