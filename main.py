from collections import defaultdict

from task import Task


from funkcje import add, remove, show, new

tasks = []
while True:
    dzialanie = input("Enter the action you want to perform (add/remove/show/new/exit) ")
    match dzialanie.lower():
        case "add":
            taskname=input("Enter the action name ")
            add(taskname,tasks)

        case "remove":
            taskname = input("Enter the action name you have already done")
            remove(taskname,tasks)
        case "show":
            show(tasks)
        case "new":
            new(tasks)
        case "exit":
            break
        case "nothing":
            break
        case _:
            print("Invalid command")



