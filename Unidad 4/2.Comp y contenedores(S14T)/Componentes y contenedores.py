import tkinter as tk
from tkinter import ttk

# Crear la ventana principal-------
root = tk.Tk()
root.title("ST14")
root.geometry("600x550")

# Crear una lista para mostrar los datos agregados como se especifico en la tarea(TreeView)------
tree = ttk.Treeview(root, columns=("fecha", "hora", "descripcion"), show="headings")
tree.heading("fecha",text="fecha")
tree.heading("hora", text="hora")
tree.heading("descripcion", text="descripcion")

tree.pack(pady=10, fill="both", expand=True)

# Crear un campo de entrada\frame---------
frame_entry= tk.Frame(root)
frame_entry.pack(pady=10)

# labels\data "identicadores"-----
tk.Label(frame_entry, text="Fecha ").grid(row=0,column=0)
entry_fecha=tk.Entry(frame_entry)
entry_fecha.grid(row=0,column=1)

#button
frame_button= tk.Frame(root)
frame_button.pack(pady=5)

# Crear un botón "Agregar"---                        modificacion  mi gusto >.<
boton_agregar = tk.Button(frame_button, text="Agregar", command="agregar_evento", background="yellow", font="Forte")
boton_agregar.grid(row=0,column=0,padx=4)

boton_limpiar = tk.Button(root, text="Limpiar", command="limpiar", background="Brown", font="Forte")
boton_limpiar.pack(pady=20)

# Función para agregar datos a la lista
def agregar_evento():
    fecha=entry_fecha.get()
#\\\\\\
    if fecha:
        tree.insert("","end",values=(fecha))

#

boton_agregar.config(command=agregar_evento())

# Ejecutar la aplicacion------
root.mainloop()
