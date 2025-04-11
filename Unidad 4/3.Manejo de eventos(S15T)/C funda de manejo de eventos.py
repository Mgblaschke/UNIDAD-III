import tkinter as tk
from tkinter import ttk, messagebox

class MiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ST15")
        self.root.geometry("400x500")

        # Crear etiquetas nombre
        etiqueta = tk.Label(root, text="TAREA:", font="Castellar")
        etiqueta.pack(pady=5)

        self.task_list = []

        # Entrada de nueva tarea
        self.entry_task = tk.Entry(root, width=40)
        self.entry_task.pack(pady=10)
        self.entry_task.bind("<Return>", lambda event: self.add_task())

        # Crear etiquetas comentario
        etiqueta = tk.Label(root, text="DESCRIPCION:", font="Castellar")
        etiqueta.pack(pady=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=30, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Botones
        self.add_btn = tk.Button(root, text="Añadir Tarea", width=20, command=self.add_task, background="yellow", font="Forte")
        self.add_btn.pack(pady=5)

        self.complete_btn = tk.Button(root, text="Marcar como Completada", width=30, command=self.complete_task, background="Brown", font="Forte")
        self.complete_btn.pack(pady=5)

        self.delete_btn = tk.Button(root, text="Eliminar Tarea", width=20, command=self.delete_task, background="red", font="Forte")
        self.delete_btn.pack(pady=5)

        # Asignación de teclas --------No descrita en la tarea

        self.root.bind("<Escape>", lambda event: self.root.quit())
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())

#FUNCIONES
        #ANADIR TAREA
    def add_task(self, event=None):
        task = self.entry_task.get().strip()
        if task:
            self.task_list.append({'task': task, 'completed': False})
            self.update_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Por favor, escribe una tarea.")

        # TAREA COMPLETADA
    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_list[index]['completed'] = not self.task_list[index]['completed']
            self.update_listbox()
        else:
            messagebox.showwarning("Ninguna tarea seleccionada", "Selecciona una tarea para marcar como completada.")

    # TAREA ELIMINADA
    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.task_list[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Ninguna tarea seleccionada", "Selecciona una tarea para eliminar.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for item in self.task_list:
            display = item['task']
            if item['completed']:
                display += " ✅"
            self.task_listbox.insert(tk.END, display)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = MiApp(root)
    root.mainloop()
