
# mini_todo.py
name=input("username; ")
print(f"welcome {name}")

def add_task(tasks):
    title = input("Enter a new task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    tasks.append({"title": title, "completed": False})
    print(f"Added: {title}")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not done"
        print(f"{idx}. [{status}] {task['title']}")
    print()

def complete_task(tasks):
    if not tasks:
        print("No tasks to complete.")
        return
    view_tasks(tasks)
    try:
        choice = int(input("Mark which task as completed (number): "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            print(f"Marked as completed: {tasks[choice - 1]['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks(tasks)
    try:
        choice = int(input("Delete which task (number): "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    menu = (
        "\nProject Tasks:\n"
        "1. Add a new task\n"
        "2. View all tasks\n"
        "3. Mark a task as completed\n"
        "4. Delete a task\n"
        "5. Exit\n"
    )

    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main()

