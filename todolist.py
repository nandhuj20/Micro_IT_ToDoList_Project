# Simple To-Do List App in Python

todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks added yet.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(todo_list, start=1):
            status = "✔ Done" if task['done'] else "✘ Not Done"
            print(f"{idx}. {task['task']} [{status}]")

def add_task():
    task_name = input("Enter task: ").strip()
    if task_name:
        todo_list.append({"task": task_name, "done": False})
        print("Task added.")
    else:
        print("Task can't be empty!")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]['done'] = True
            print("Marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ").strip()

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye! Stay productive.")
        break
    else:
        print("Invalid choice. Try again.")
