import json

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def list_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} {'(Done)' if task['done'] else ''}")

def add_task(tasks, task_text):
    tasks.append({"task": task_text, "done": False})

def mark_task_done(tasks, task_index):
    if 0 < task_index <= len(tasks):
        tasks[task_index - 1]["done"] = True
    else:
        print("Invalid task index.")

def delete_task(tasks, task_index):
    if 0 < task_index <= len(tasks):
        del tasks[task_index - 1]
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. List tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            task_text = input("Enter the task: ")
            add_task(tasks, task_text)
            save_tasks(tasks)
        elif choice == "3":
            list_tasks(tasks)
            task_index = int(input("Enter the task index to mark as done: "))
            mark_task_done(tasks, task_index)
            save_tasks(tasks)
        elif choice == "4":
            list_tasks(tasks)
            task_index = int(input("Enter the task index to delete: "))
            delete_task(tasks, task_index)
            save_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
