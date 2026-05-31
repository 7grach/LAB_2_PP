from storage import load_tasks, save_tasks

def show_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()

    if 0 < index <= len(tasks):
        tasks.pop(index - 1)
        save_tasks(tasks)