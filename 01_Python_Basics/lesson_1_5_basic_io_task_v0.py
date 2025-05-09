"""
Lesson 1.5: Basic I/O & Task Manager v0

This lesson covers:
1. Basic input/output operations
2. String formatting
3. Simple task management
4. Basic program structure

This is the first version of our task manager that:
- Stores tasks in a list
- Allows adding new tasks
- Displays all tasks
- Uses basic I/O operations
"""

def display_menu():
    """Display the main menu"""
    print("\nTask Manager v0")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Exit")

def add_task(tasks):
    """Add a new task to the list"""
    task = input("Enter task description: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("No tasks found!")
        return
    
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def main():
    """Main program loop"""
    tasks = []  # Store tasks in a list
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 