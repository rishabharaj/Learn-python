"""
Lesson 2.3: Task Manager Data v1

This lesson covers:
1. Using dictionaries for structured data
2. Lists of dictionaries
3. Data manipulation
4. Basic task management with structured data

This version of the task manager:
- Stores tasks as dictionaries in a list
- Each task has description and completion status
- Allows adding, viewing, and marking tasks as complete
"""

def display_menu():
    """Display the main menu"""
    print("\nTask Manager v1")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as complete")
    print("4. Exit")

def add_task(tasks):
    """Add a new task to the list"""
    description = input("Enter task description: ")
    task = {
        "description": description,
        "completed": False
    }
    tasks.append(task)
    print(f"Task '{description}' added successfully!")

def view_tasks(tasks):
    """Display all tasks with their status"""
    if not tasks:
        print("No tasks found!")
        return
    
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['description']}")

def mark_task_complete(tasks):
    """Mark a task as complete"""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("\nEnter task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main program loop"""
    tasks = []  # Store tasks as dictionaries in a list
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 