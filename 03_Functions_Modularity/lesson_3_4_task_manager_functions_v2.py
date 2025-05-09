"""
Lesson 3.4: Task Manager Functions v2

This lesson covers:
1. Function-based task management
2. Modular code organization
3. Function composition
4. Error handling
5. Type hints

This version of the task manager:
- Uses functions for all operations
- Implements error handling
- Uses type hints
- Has a more modular structure
"""

from typing import List, Dict, Optional

# Type aliases
Task = Dict[str, str]
TaskList = List[Task]

def create_task(description: str, priority: str = "medium") -> Task:
    """Create a new task dictionary
    
    Args:
        description: The task description
        priority: The task priority (low, medium, high)
        
    Returns:
        A dictionary representing the task
    """
    return {
        "description": description,
        "priority": priority,
        "status": "pending"
    }

def add_task(tasks: TaskList, description: str, priority: str = "medium") -> None:
    """Add a new task to the list
    
    Args:
        tasks: The list of tasks
        description: The task description
        priority: The task priority
    """
    task = create_task(description, priority)
    tasks.append(task)
    print(f"Task '{description}' added successfully!")

def view_tasks(tasks: TaskList, filter_status: Optional[str] = None) -> None:
    """Display all tasks with optional filtering
    
    Args:
        tasks: The list of tasks
        filter_status: Optional status to filter by
    """
    if not tasks:
        print("No tasks found!")
        return
    
    print("\nYour Tasks:")
    filtered_tasks = (
        tasks if filter_status is None
        else [t for t in tasks if t["status"] == filter_status]
    )
    
    for i, task in enumerate(filtered_tasks, 1):
        print(f"{i}. [{task['priority']}] {task['description']} ({task['status']})")

def update_task_status(tasks: TaskList, task_num: int, new_status: str) -> bool:
    """Update a task's status
    
    Args:
        tasks: The list of tasks
        task_num: The task number to update
        new_status: The new status
        
    Returns:
        True if successful, False otherwise
    """
    if not 1 <= task_num <= len(tasks):
        print("Invalid task number!")
        return False
    
    tasks[task_num - 1]["status"] = new_status
    print("Task status updated successfully!")
    return True

def get_valid_input(prompt: str, valid_choices: List[str]) -> str:
    """Get valid input from user
    
    Args:
        prompt: The prompt to display
        valid_choices: List of valid choices
        
    Returns:
        The user's valid choice
    """
    while True:
        choice = input(prompt).lower()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please choose from: {', '.join(valid_choices)}")

def display_menu() -> None:
    """Display the main menu"""
    print("\nTask Manager v2")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. View pending tasks")
    print("4. Mark task as complete")
    print("5. Exit")

def main() -> None:
    """Main program loop"""
    tasks: TaskList = []
    
    while True:
        display_menu()
        choice = get_valid_input("Enter your choice (1-5): ", ["1", "2", "3", "4", "5"])
        
        if choice == "1":
            description = input("Enter task description: ")
            priority = get_valid_input("Enter priority (low/medium/high): ", 
                                     ["low", "medium", "high"])
            add_task(tasks, description, priority)
            
        elif choice == "2":
            view_tasks(tasks)
            
        elif choice == "3":
            view_tasks(tasks, "pending")
            
        elif choice == "4":
            view_tasks(tasks)
            if tasks:
                try:
                    task_num = int(input("Enter task number to mark as complete: "))
                    update_task_status(tasks, task_num, "completed")
                except ValueError:
                    print("Please enter a valid number!")
                    
        elif choice == "5":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main() 