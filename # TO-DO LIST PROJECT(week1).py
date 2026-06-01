# TO-DO LIST PROJECT

# Empty list to store tasks
tasks = []

# Function to add tasks
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!\n")

# Function to view tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks):
            print(index + 1, ".", task)
        print()

# Function to remove tasks
def remove_task():
    view_tasks()

    if len(tasks) != 0:
        try:
            task_number = int(input("Enter task number to remove: "))
            
            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)
                print(removed, "removed successfully!\n")
            else:
                print("Invalid task number.\n")

        except:
            print("Please enter a valid number.\n")

# Main Program
while True:

    print("===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        print("Exiting program...")
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.\n")
        