#Creacion tkinter
import tkinter as tk
from tkinter import ttk

# Función para agregar datos a la lista
def agregar_dato():
    dato = campo_texto.get()  # Obtener el texto del campo de entrada
    if dato:
        lista_datos.insert(tk.END, dato)  # Insertar el dato en la lista
        campo_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        ttk.showwarning("Advertencia", "Por favor, ingresa un dato.")

# Función para limpiar la lista y el campo de texto
def limpiar():
    campo_texto.delete(0, tk.END)  # Limpiar el campo de texto
    lista_datos.delete(0, tk.END)  # Limpiar la lista de datos

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación de Datos")
root.geometry("300x450")

# Crear etiquetas
etiqueta = tk.Label(root, text="Ingresa un dato:")
etiqueta.pack(pady=10)

# Crear un campo de texto para ingresar datos
campo_texto = tk.Entry(root, width=30)
campo_texto.pack(pady=5)

# Crear un botón "Agregar"---                        modificacion  mi gusto >.<
boton_agregar = tk.Button(root, text="Agregar", command=agregar_dato, background="yellow", font="Castellar")
boton_agregar.pack(pady=10)

# Crear una lista para mostrar los datos agregados como se especifico en la tarea
lista_datos = tk.Listbox(root, width=30, height=10)
lista_datos.pack(pady=10)

# Crear un botón "Limpiar"-----
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar, background="red", font="Forte")
boton_limpiar.pack(pady=20)

# Ejecutar la aplicacion------
root.mainloop()
