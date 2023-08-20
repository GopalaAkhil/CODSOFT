from tkinter import *
from tkinter import messagebox

# Function to add a new task to the list
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")
# Function to delete the selected task from the list
def deleteTask():
    lb.delete(ANCHOR)

# Function to update the selected task with a new task name
def updateTask():
    try:
        index = lb.curselection()[0]
        task = my_entry.get()
        if task != "":
            lb.delete(index)
            lb.insert(index, task)
            my_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Please enter a new task name.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Create the main window
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To-Do-List')
#ws.iconbitmap("todolist.ico")
ws.config(bg='#dfe6e9')
ws.resizable(width=False, height=False)

# Create a frame to hold the Listbox and Scrollbar
frame = Frame(ws)
frame.pack(pady=10)

# Create a Listbox to display tasks
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#2d3436',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)


# List of tasks (if any) can be added here
task_list = [
    
    ]

for item in task_list:
    lb.insert(END, item)

# Create a Scrollbar and link it to the Listbox
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# Create an Entry widget to enter new tasks
my_entry = Entry(
    ws,
    font=('times', 24),
    bd=0,
    bg='#c0c0c0',  
    highlightthickness=0,
    insertbackground='#2d3436',

    )

my_entry.pack(pady=20)


# Create a frame to hold the buttons
button_frame = Frame(ws)
button_frame.pack(pady=20)

# Button style for the "Add Task" button
addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#00b894',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# Button style for the "Delete Task" button
delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#d63031',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# Button style for the "Update Task" button
updateTask_btn = Button(
    button_frame,
    text='Update Task',
    font=('times 14'),
    bg='#0984e3',
    padx=20,
    pady=10,
    command=updateTask
)

updateTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# Start the main event loop
ws.mainloop()
