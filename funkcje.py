from task import Task

def add(taskname, tasks, category, priority):
    exists = any(task.taskname == taskname for task in tasks[:])
    if exists:
        print("Task has been already added ")
    else:
        new_task = Task(taskname,category,priority)
        tasks.append(new_task)


def remove(taskname, tasks):
    for task in tasks[:]:
        if task.taskname.lower() == taskname.lower():
            tasks.remove(task)


def show(tasks):
    for task in sorted(tasks, key=lambda x: x.priority):
        print("task: ",task.taskname, " category:", task.category, "priority:" ,task.priority)
def wyszukaj(taskname,tasks):
    exists = any(task.taskname == taskname for task in tasks[:])
    if exists:
        print("Task has been already added ")
    else:
        print("Task not found")



def new(tasks):
    for task in tasks[:]:
        tasks.remove(task)
    print("List has been cleared ")
def pomoc (tasks):
    print("""List of all commands:
          add - add a new task
          remove - remove a task
          show - show a list of tasks
          new - create a new list of tasks
          exit - exit the program
          help - a list of all commands in app
          category + word - adding a task to a given category
          find + word - checking if a task already exists
          priority - add to task priority
          save - save your task list in a file""")
def save(tasks):
    import os
    sciezka = os.path.join(os.path.expanduser("~"), "Desktop", "zadania.txt")
    with open(sciezka, "w", encoding="utf-8") as plik:
        for task in tasks:
            plik.write("TO-DO LIST:\n")
            plik.write(f"{task.taskname} | {task.category} | priorytet: {task.priority}\n")
