import tkinter as tk
from tkinter import ttk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ST16")
        self.root.geometry("400x350")

        self.tasks = []

        # Campo de entrada---------------
        self.entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda event: self.add_task())

        # Asignacion de Botones------------
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        self.add_btn = tk.Button(btn_frame, text="Añadir", command=self.add_task, background="yellow", font="Forte")
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(btn_frame, text="Completar", command=self.complete_task, background="Brown", font="Forte")
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task, background="red", font="Forte")
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Lista de tareas----------
        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, font=("Helvetica", 14), activestyle='none')
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Asociación de teclas-------
        #Cierra la aplicación.
        self.root.bind("<Escape>", lambda event: self.root.quit())
        # Marcar/desmarcar tarea seleccionada como completada.
        self.root.bind("<c>", lambda event: self.complete_task())
        #Eliminar tarea seleccionada.
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "done": False})
            self.entry.delete(0, tk.END)
            self.update_listbox()

    def complete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.update_listbox()

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task["text"]
            if task["done"]:
                display_text = f"✔ {display_text}"
                self.listbox.insert(tk.END, display_text)
                self.listbox.itemconfig(tk.END, fg="gray", selectforeground="gray")
            else:
                self.listbox.insert(tk.END, display_text)
                self.listbox.itemconfig(tk.END, fg="black", selectforeground="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
