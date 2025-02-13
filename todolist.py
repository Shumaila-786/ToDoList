# Topics: tkinter, pickle, listbox widget, grid geometry manager, tkinter.messagebox(error windows), Try/Except block
#1 import tkinter library which will  get a window for us
import tkinter
import tkinter.messagebox
import pickle                #It's a module which will help us Save our tasks in a separate file
#2  Assign a variable window or Root which will have whatever we're getting from tkinter
window = tkinter.Tk()
window.title("To-Do List by Shumaila")

#6 defining command add_task in line 22
def add_task():

   
    task = entry_task.get()                      # step after #5 gets task from the entry task box and insert it  to the listbox  at the end
    print(f"Task entered: {task}")  # This will print the task in the terminal
    if task != "":                               #if-else cond for warningmessage   
       listbox_tasks.insert(tkinter. END, task)   
   
   #7 Adding a delete function that removes the entered text from the entry box all the way to end 
       entry_task.delete(0, tkinter.END)
    else:
       tkinter.messagebox.showwarning(title="warning", message="You must enter a task")

#8 defining command, delete_task, 
def delete_task():
    
#9 Try  and except block : tries  the folowwing and if it gives an error then it   will do 'except':if there is no task selected, this willl show an error  
    try:
         task_index = listbox_tasks.curselection()[0]
         listbox_tasks.delete(task_index)
    except:
         tkinter.messagebox.showwarning(title="warning", message="You must select a task")

# defining command, load_tasks   

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.file", "rb"))                   # this will read the saved file, 'read binary' and load it's data 
        listbox_tasks.delete(0, tkinter.END)                            #this will stop loading the tasks repeatedly
        for task in tasks:                                              # this will get the data into the llistbox
            listbox_tasks.insert(tkinter.END, task) 
    except:
        tkinter.messagebox.showwarning(title="warning", message="File not found")
#Last step :  here we will delete the file manually and try and load it this will give an error in the terminal, in order to avoid that we will add a Try-Except on our Load block,

#Last step so after except we will add the same error message we added earlier "tkinter.messagebox.showwarning(title="warning", message="cannot find task.data")"
  
# defining command, save_tasks    
def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())             
    #print (tasks) #print a Tuple in terminal
    pickle.dump(tasks, open('tasks.file', 'wb'))                     # this will dump the tasks from the listbox to a file called tasks.data with 'write binary'

  

# Create GUI

listbox_tasks = tkinter.Listbox(window, height=3, width=50)       # Ttkinter.Listbox willl get the Listbox widget from Tkinter;Listbox is a class and is always an Uppercase
listbox_tasks.pack()

#4 Adding a task entry box 
entry_task = tkinter.Entry(window, width=50)
entry_task.pack()                                                 # pack() is a geometry manager in Tkinter. It controls where the widget is placed in the window.

#5 Add buttons for my tasks using class from tkinter, 'Button'

button_add_task = tkinter.Button(window, text="Add Task", width=48, command=add_task)
button_add_task.pack()
button_delete_task = tkinter.Button(window, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()
button_load_task = tkinter.Button(window, text="Load Tasks", width=48, command=load_tasks)
button_load_task.pack()
button_save_task = tkinter.Button(window, text="Save Tasks", width=48, command=save_tasks)
button_save_task.pack()
window.mainloop()