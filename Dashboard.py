import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/1.1. Tecnicas de Programacion/1.1.2 Tecnicas de programacion.py',
        '2': 'Unidad 1/1.1. Tecnicas de Programacion/1.1.3 herencia.py',
        '3': 'Unidad 1/1.1. Tecnicas de Programacion/1.1.4 polimorfismo.py',
        '4': 'Unidad 1/1.1. Tecnicas de Programacion/1.1.5 encapsulamiento.py',
        '5': 'Unidad 1/1.2. Programacion tradicional frente a POO/1.2-1. Ejemplo - POO.py',
        '6': 'Unidad 1/1.2. Programacion tradicional frente a POO/1.2-2. Ejemplo Programacion tradicional.py',
        '7': 'Unidad 1/1.3. Características de la POO(TAREAS4)/EjemploAvion_azafata.py',
        '8': 'Unidad 1/1.3. Características de la POO(TAREAS4)/EjemplosMundoReal2_POO..py',
        '9': 'Unidad 1/1.3. Características de la POO(TAREAS4)/EjemploTrailer,inicio.py',
        '10': 'Unidad 2/1.1. Tipos de Datos e Identificadores/1.1.2 Tipos de datos, Identificadores.py',
        '11': 'Unidad 2/1.2. C, O, H, E y P(TAREAS6)/Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '12': 'Unidad 2/1.3. Constructores y Destructores(TAREAS7)/CONTRUCTOR&DESTRUCTOR.py',

        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()