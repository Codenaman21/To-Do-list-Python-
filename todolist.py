import json

# File to save the to-do list
todo_file = "todo_list.json"

# Load existing to-do list from file
def load_todo_list():
    try:
        with open(todo_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_todo_list(todo_list):
    with open(todo_file, "w") as file:
        json.dump(todo_list, file, indent=4)

def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def main():
    todo_list = load_todo_list()

    while True:
        print("\nTo-Do List Options:")
        print("1. View To-Do List")
        print("2. Add a Task")
        print("3. Remove a Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            task = input("Enter the task to add: ").strip()
            if task:
                todo_list.append(task)
                save_todo_list(todo_list)
                print("Task added!")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            display_todo_list(todo_list)
            try:
                task_num = int(input("Enter the task number to remove: ").strip())
                if 1 <= task_num <= len(todo_list):
                    removed_task = todo_list.pop(task_num - 1)
                    save_todo_list(todo_list)
                    print(f"Task '{removed_task}' removed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 4.")

if __name__ == "__main__":
    main()
