# To-Do List using functions

tasks = []

while True:
    print("******************")
    print("To-Do List Menu:")
    print("******************\n")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove  task")
    print("4. Exit\n")
    print("******************")
    
    choice = input("Choose an option (1-4):")
    print("******************\n")
    
    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)                                  # .append() method is used to add task to the list
        print(f'Task "{task}" added to the list.\n')
    elif choice == '2':
        if not tasks:
            print("No tasks in the list.\n")
        else:
            print("Your To-Do List:")
            for f, j in enumerate(tasks, start=1):          # .enumerate() function is used to get the index and value of each task in the list, starting from 1
                print(f"{f}. {j}")
            print()
    elif choice == '3':
        if not tasks:
            print("No tasks to remove.\n")
        else:
            print("Your To-Do List:")
            for f, j in enumerate(tasks, start=1):
                print(f"{f}. {j}")
            try:
                task_num = int(input("Enter the number of the task to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)                          # .pop() method is used to remove the task from the list and return it, task_num - 1 is used because list indices start at 0
                    print(f'Task "{removed_task}" removed from the list.\n')
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("Please enter a valid number.\n")
    elif choice == '4':
        print("Thanks for using the To-Do List, Goodbye!\n")
        print("******************")
        break                                                       # break statement is used to exit the loop when the user chooses to exit
    else:
        print("Invalid option. Please choose 1-4.\n")
