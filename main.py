from task_manager import show_tasks, add_task, delete_task
while True:

    print("\nTODO APP")
    print("1 - Show tasks")
    print("2 - Add task")
    print("3 - Delete task")
    print("4 - Exit app")

    choice = input("Choose: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        text = input("Task text: ")
        add_task(text)

    elif choice == "3":
        index = int(input("Task number: "))
        delete_task(index)

    elif choice == "4":
        break
