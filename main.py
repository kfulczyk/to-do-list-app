from collections import defaultdict

from task import Task


def isgood(priority):
    if priority == "1" or priority == "2" or priority == "3":
        return True
    else: return False


from function import add, remove, show, new, pomoc, wyszukaj, save, show_category

tasks = []
while True:
    dzialanie = input("Enter the action you want to perform (show category/add/remove/show/new/exit/help/find/save(all taks in a file) ")
    match dzialanie.lower():
        case "add":
            taskname=input("Enter the action name")
            category=input("Enter the category of the task")
            priority=input("Enter the priority of the task (1-highest) (2-medium) (3-lowest)")
            if ( isgood(priority)==False ):
                print("Priority must be between 1-3")



            add(taskname,tasks,category,priority)

        case "remove":
            taskname = input("Enter the action name you have already done")
            remove(taskname,tasks)
        case "show":
            show(tasks)
        case "new":
            new(tasks)
        case "exit":
            break
        case "help":
            pomoc(tasks)
        case "find":
            taskname = input("Enter the action name")
            wyszukaj(taskname.lower(),tasks)
        case "save":
            save(tasks)
        case "show category":
            show_category(tasks)
        case _:
            print("Invalid command")
