import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
import os

root = tk.Tk()
root.title("Tasks and Homeworks")
root.geometry("480x560")

#styles
bg_color  = "#1e1e2f"  # fondo general
fg_color  = "#ffffff"  # texto
btn_color = "#3a7ff6"  # botones
entry_bg  = "#2a2a3f"  # fondo de los inputs
list_bg   = "#2a2a3f"  # fondo de la lista
font_text = "Arial", 11# fuente del texto normal

root.configure(background=bg_color)

label = tk.Label(root, text="Hello again Mr.Jesus", bg=bg_color, fg=fg_color,
                 font=("Arial", 16, "bold"))
label.pack(pady=5)

tasks = []

tasks_names = (tk.Label(root,
                       text="Enter tasks name:",
                       bg=bg_color,
                       fg=fg_color,
                       font=font_text))
tasks_names.pack()
name = tk.Entry(root, bg=entry_bg, fg=fg_color, insertbackground=fg_color, width=50)
name.pack()


task_text = tk.Label(root, text="Enter your task:", bg=bg_color, fg=fg_color, font=font_text)
task_text.pack()
task = tk.Entry(root, bg=entry_bg, fg=fg_color, insertbackground=fg_color, width=50)
task.pack()


deadline_text = tk.Label(root, text="Enter deadline:", bg=bg_color, fg=fg_color, font=font_text)
deadline_text.pack()
cal = Calendar(root, selectmode="day", date_pattern="dd/mm/yyyy",
               background=entry_bg, foreground=fg_color,
               headersbackground="#3a3a5f", headersforeground=fg_color,
               selectbackground=btn_color, selectforeground=fg_color,
               normalbackground=entry_bg, normalforeground=fg_color,
               weekendbackground=entry_bg, weekendforeground="#ff6b6b")
cal.pack(pady=5)

def add_task():
    task_name = task.get().strip()
    deadline = cal.get_date()

    if not task_name:
        messagebox.showerror("Error", "Please enter a valid task!")
        return

    tasks.append({"name": task_name, "deadline": deadline})
    task_listbox.insert(tk.END, f"{task_name} -- {deadline}")
    task.delete(0, tk.END)

def delete_fun():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a task to delete!")
        return
    index = selected[0]
    tasks.pop(index)
    task_listbox.delete(index)

def export_to_txt():

    if not tasks:
        messagebox.showerror("Error", "No task to export yet!")
        return

    file_name = name.get().strip()
    if not file_name:
        messagebox.showerror("Error", "Remember the file name!")

    sorted_tasks = sorted(tasks, key=lambda t: datetime.strptime(t["deadline"], '%d/%m/%Y'))

#endswith, Metodo de strings que verifica si un texto termina con cierta cadena.
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    with open(file_name, "w") as f:
        for i, item in enumerate(sorted_tasks, 1):
            f.write(f"{i}. {item['name']} - {item['deadline']}\n")

    messagebox.showinfo("Done!", f"Saved at: {os.path.abspath(file_name)}")

tk.Button(root, text="Add task", command=add_task,
          bg=btn_color, fg=fg_color, relief="flat").pack(pady=2)
tk.Button(root, text="Delete task", command=delete_fun, bg="#e05555", fg=fg_color, relief="flat").pack(pady=2)
tk.Button(root, text="Export tasks", command=export_to_txt, bg="#3ab87f", fg=fg_color, relief="flat").pack(pady=2)

tk.Label(root, text="Your tasks:", bg=bg_color, fg=fg_color).pack()

#tk.Listbox Widget de Tkinter que muestra una lista de elementos seleccionables.
task_listbox = tk.Listbox(root, width=50, height=6,
                          bg=list_bg, fg=fg_color,
                          selectbackground=btn_color,
                          selectforeground=fg_color,
                          relief="flat")
task_listbox.pack(pady=5)

root.mainloop()

