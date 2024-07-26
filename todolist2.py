tasks = []

# task functions

def addTask():
        task = input("Please enter a task: ")
        tasks.append(task)
        print(f"Task '{task}' added to the list.")

def listTasks():
        if not tasks:
                    print("There are no tasks currently.")
        else:
                    print("Current Tasks:")
                    for index, task in enumerate(tasks, start=1):
                                print(f"Task #{index}. {task}")

def deleteTask():
        listTasks()
        if not tasks:
        return
