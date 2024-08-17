import os
os.system("clear")

tasks = []  # Ro'yxatni yaratish

while True:
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        description = input("Enter task description: ")
        priority = input("Enter task priority: ")
        tasks.append({"description": description, "priority": priority, "status": "Not Done"})
        print("Task added successfully!")
        print()
    elif choice == 2:
        if not tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks):
                print(f"Task {i + 1}: {task['description']}, Priority: {task['priority']}, Status: {task['status']}")
                
    elif choice == 3:
        index = int(input("Enter task index to complete: ")) - 1
        tasks[index]['status'] = "Done"
        print("Task completed successfully!")
        
    elif choice == 4:
        index = int(input("Enter task index to remove: ")) - 1
        tasks.pop(index)
        print("Task removed successfully!")
        
    elif choice == 5:
        print("Exiting...")
        break
        
    else:
        print("Please enter a number between 1 and 5.")
