import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("There are no tasks.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\nSelect an action:")
        print("1. Show tasks")
        print("2. Add a task")
        print("3. Delete an issue")
        print("4. Exit")

        choice = input("Enter the number: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Select a task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            index = int(input("Enter the issue number to delete: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                save_tasks(tasks)
            else:
                print("Incorrect number")
        elif choice == "4":
            break
        else:
            print("Incorrect input")

if __name__ == "__main__":
    main()
