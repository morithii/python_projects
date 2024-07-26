tasks = []

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
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if 1 <= taskToDelete <= len(tasks):
            deleted_task = tasks.pop(taskToDelete - 1)
            print(f"Task '{deleted_task}' has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found")
    except ValueError:
        print("Invalid input. Please enter a number.")

def updateTask():
    listTasks()
    if not tasks:
        return
    try:
        taskToUpdate = int(input("Enter the # of the task to update: "))
        if 1 <= taskToUpdate <= len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[taskToUpdate - 1] = new_task
            print(f"Task #{taskToUpdate} has been updated.")
        else:
            print(f"Task #{taskToUpdate} was not found")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("Welcome to the python to-do-list-app!!!")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Update a task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            updateTask()
        elif choice == "5":
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye!!!!")
