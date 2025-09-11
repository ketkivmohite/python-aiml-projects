def save_tasks_to_file(tasks_list):
    with open("tasks.txt","w") as file:
        for task in tasks_list:
            file.write(task + "\n")

tasks = []
while True:
    print("\n Choose an option: ")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        task_to_add = input("What task do you want to add?")
        tasks.append(task_to_add)
        save_tasks_to_file(tasks)
        print(f"'{task_to_add}' was added to your list")

    elif choice =='2':
        print("\n---Your Tasks---")
        for task in tasks:
            print(task)
        print("----------------")

    elif choice == '3':
        print("GoodBye!")
        break

    else:
        print("Invalid Choice. Please enter 1,2 or 3.")

