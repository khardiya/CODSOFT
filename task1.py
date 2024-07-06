import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []

        # Frame for the Listbox and Scrollbar
        frame = tk.Frame(root)
        frame.pack(pady=20)

        self.task_listbox = tk.Listbox(frame, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Frame for the Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)
        
        add_button = ttk.Button(button_frame, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=0, padx=10)
        
        remove_button = ttk.Button(button_frame, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=0, column=1, padx=10)
        
        mark_button = ttk.Button(button_frame, text="Mark Completed", command=self.mark_completed)
        mark_button.grid(row=0, column=2, padx=10)
        
        edit_button = ttk.Button(button_frame, text="Edit Task", command=self.edit_task)
        edit_button.grid(row=0, column=3, padx=10)
        
        save_button = ttk.Button(button_frame, text="Save Tasks", command=self.save_tasks)
        save_button.grid(row=1, column=0, columnspan=2, pady=10)
        
        load_button = ttk.Button(button_frame, text="Load Tasks", command=self.load_tasks)
        load_button.grid(row=1, column=2, columnspan=2, pady=10)
        
        self.load_tasks()

    def add_task(self):
        task = simpledialog.askstring("Task", "Enter the task:")
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Remove Task", "No task selected.")
            
    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]['task']
            new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=task)
            if new_task:
                self.tasks[selected_task_index[0]]['task'] = new_task
                self.update_listbox()
        else:
            messagebox.showwarning("Edit Task", "No task selected.")
            
    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]['completed'] = not self.tasks[selected_task_index[0]]['completed']
            self.update_listbox()
        else:
            messagebox.showwarning("Mark Completed", "No task selected.")
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks, 1):
            display_text = f"{i}. {task['task']}" + (" (Completed)" if task['completed'] else "")
            self.task_listbox.insert(tk.END, display_text)
            
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task['task']}|{task['completed']}\n")
        messagebox.showinfo("Save Tasks", "Tasks saved successfully.")
        
    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                self.tasks = []
                for line in file.readlines():
                    parts = line.strip().split("|")
                    if len(parts) == 2:
                        task, completed = parts
                        self.tasks.append({"task": task, "completed": completed == 'True'})
            self.update_listbox()
        else:
            self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
