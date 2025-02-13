# To-Do List Application (Tkinter + Pickle)

## Overview
This Python script creates a simple **To-Do List** application using **Tkinter** (for the graphical user interface) and **Pickle** (for saving and loading tasks). It allows users to **add, delete, save, and load tasks**.

---

## Code Breakdown

### **1. Importing Required Libraries**
```python
import tkinter
import tkinter.messagebox
import pickle
```
- **Tkinter**: Used to create the GUI.
- **tkinter.messagebox**: Used to display warning messages.
- **Pickle**: Used to save and load tasks in a file.

---

### **2. Initializing the Tkinter Window**
```python
window = tkinter.Tk()
window.title("To-Do List by Shumaila")
```
- **`tkinter.Tk()`** creates the main application window.
- **`title()`** sets the window title.

---

### **3. Function to Add Tasks**
```python
def add_task():
    task = entry_task.get()
    print(f"Task entered: {task}")
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning", message="You must enter a task")
```
- Retrieves the task from the **entry box**.
- Adds it to the **Listbox** if it's not empty.
- Clears the entry box after adding.
- Shows a warning if the input is empty.

---

### **4. Function to Delete Tasks**
```python
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]  # Get selected task
        listbox_tasks.delete(task_index)  # Delete from Listbox
    except:
        tkinter.messagebox.showwarning(title="Warning", message="You must select a task")
```
- Removes the **selected** task from the **Listbox**.
- Uses `try-except` to handle cases where no task is selected.

---

### **5. Function to Load Tasks from File**
```python
def load_tasks():
    try:
        tasks = pickle.load(open("tasks.file", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning", message="File not found")
```
- Reads saved tasks from **tasks.file**.
- Clears the **Listbox** before loading tasks.
- Uses `try-except` to handle cases where the file is missing.

---

### **6. Function to Save Tasks to File**
```python
def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open('tasks.file', 'wb'))
```
- Retrieves all tasks from the **Listbox**.
- Saves them to **tasks.file** using Pickle.

---

### **7. Creating the GUI Components**

#### **Listbox to Display Tasks**
```python
listbox_tasks = tkinter.Listbox(window, height=3, width=50)
listbox_tasks.pack()
```
- A **Listbox widget** is created to display the tasks.

#### **Entry Widget for User Input**
```python
entry_task = tkinter.Entry(window, width=50)
entry_task.pack()
```
- Allows users to enter new tasks.

#### **Buttons for Actions**
```python
button_add_task = tkinter.Button(window, text="Add Task", width=48, command=add_task)
button_add_task.pack()
```
- Calls the `add_task()` function when clicked.

Similarly, buttons for **Delete, Load, and Save** are created:
```python
button_delete_task = tkinter.Button(window, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_load_task = tkinter.Button(window, text="Load Tasks", width=48, command=load_tasks)
button_load_task.pack()

button_save_task = tkinter.Button(window, text="Save Tasks", width=48, command=save_tasks)
button_save_task.pack()
```

---

### **8. Running the Tkinter Event Loop**
```python
window.mainloop()
```
- Keeps the application running and responsive to user actions.

---

## **Summary**
This To-Do List app allows users to:
✅ Add tasks
✅ Delete tasks
✅ Save tasks to a file
✅ Load tasks from a file

The app is built with **Tkinter** for GUI and **Pickle** for saving/loading data. 🚀

