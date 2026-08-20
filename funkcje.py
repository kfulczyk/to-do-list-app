from task import Task

def add(taskname, tasks):
    exists = any(task.taskname == taskname for task in tasks[:])
    if exists:
        print("Task has been already added ")
    else:
        new_task = Task(taskname)
        tasks.append(new_task)


def remove(taskname, tasks):
    for task in tasks[:]:
        if task.taskname.lower() == taskname.lower():
            tasks.remove(task)


def show(tasks):
    for task in tasks[:]:
        print(task.taskname)


def new(tasks):
    for task in tasks[:]:
        tasks.remove(task)
    print("List has been cleared ")