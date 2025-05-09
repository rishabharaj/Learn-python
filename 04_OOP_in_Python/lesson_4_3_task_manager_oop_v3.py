"""
Lesson 4.3: Task Manager OOP v3

This lesson covers:
1. Object-oriented task management
2. Class-based design
3. Encapsulation
4. Inheritance
5. Polymorphism

This version of the task manager:
- Uses classes for tasks and task manager
- Implements proper encapsulation
- Uses inheritance for different task types
- Has a more organized structure
"""

from typing import List, Optional
from datetime import datetime
from abc import ABC, abstractmethod

class Task(ABC):
    """Abstract base class for tasks"""
    
    def __init__(self, description: str, priority: str = "medium"):
        """Initialize a new task
        
        Args:
            description: The task description
            priority: The task priority
        """
        self.description = description
        self.priority = priority
        self.status = "pending"
        self.created_at = datetime.now()
    
    @abstractmethod
    def get_type(self) -> str:
        """Get the task type
        
        Returns:
            The task type
        """
        pass
    
    def mark_complete(self) -> None:
        """Mark the task as complete"""
        self.status = "completed"
    
    def __str__(self) -> str:
        return (f"{self.get_type()} Task: {self.description} "
                f"(Priority: {self.priority}, Status: {self.status})")

class BasicTask(Task):
    """A basic task with no additional features"""
    
    def get_type(self) -> str:
        return "Basic"

class TimedTask(Task):
    """A task with a deadline"""
    
    def __init__(self, description: str, deadline: datetime, priority: str = "medium"):
        """Initialize a new timed task
        
        Args:
            description: The task description
            deadline: The task deadline
            priority: The task priority
        """
        super().__init__(description, priority)
        self.deadline = deadline
    
    def get_type(self) -> str:
        return "Timed"
    
    def is_overdue(self) -> bool:
        """Check if the task is overdue
        
        Returns:
            True if overdue, False otherwise
        """
        return datetime.now() > self.deadline and self.status != "completed"
    
    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str} (Deadline: {self.deadline})"

class TaskManager:
    """A class to manage tasks"""
    
    def __init__(self):
        """Initialize a new task manager"""
        self.tasks: List[Task] = []
    
    def add_task(self, task: Task) -> None:
        """Add a new task
        
        Args:
            task: The task to add
        """
        self.tasks.append(task)
        print(f"Task added: {task.description}")
    
    def get_tasks(self, status: Optional[str] = None) -> List[Task]:
        """Get tasks with optional status filter
        
        Args:
            status: Optional status to filter by
            
        Returns:
            List of matching tasks
        """
        if status is None:
            return self.tasks
        return [task for task in self.tasks if task.status == status]
    
    def mark_task_complete(self, task_index: int) -> bool:
        """Mark a task as complete
        
        Args:
            task_index: The index of the task
            
        Returns:
            True if successful, False otherwise
        """
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
            return True
        return False
    
    def view_tasks(self, status: Optional[str] = None) -> None:
        """Display tasks with optional status filter
        
        Args:
            status: Optional status to filter by
        """
        tasks = self.get_tasks(status)
        if not tasks:
            print("No tasks found!")
            return
        
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
            if isinstance(task, TimedTask) and task.is_overdue():
                print("   ⚠️ This task is overdue!")

def display_menu() -> None:
    """Display the main menu"""
    print("\nTask Manager v3")
    print("1. Add basic task")
    print("2. Add timed task")
    print("3. View all tasks")
    print("4. View pending tasks")
    print("5. Mark task as complete")
    print("6. Exit")

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

def main() -> None:
    """Main program loop"""
    manager = TaskManager()
    
    while True:
        display_menu()
        choice = get_valid_input("Enter your choice (1-6): ", 
                               ["1", "2", "3", "4", "5", "6"])
        
        if choice == "1":
            description = input("Enter task description: ")
            priority = get_valid_input("Enter priority (low/medium/high): ", 
                                     ["low", "medium", "high"])
            task = BasicTask(description, priority)
            manager.add_task(task)
            
        elif choice == "2":
            description = input("Enter task description: ")
            priority = get_valid_input("Enter priority (low/medium/high): ", 
                                     ["low", "medium", "high"])
            try:
                deadline_str = input("Enter deadline (YYYY-MM-DD HH:MM): ")
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
                task = TimedTask(description, deadline, priority)
                manager.add_task(task)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM")
                
        elif choice == "3":
            manager.view_tasks()
            
        elif choice == "4":
            manager.view_tasks("pending")
            
        elif choice == "5":
            manager.view_tasks()
            if manager.tasks:
                try:
                    task_num = int(input("Enter task number to mark as complete: "))
                    if manager.mark_task_complete(task_num - 1):
                        print("Task marked as complete!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")
                    
        elif choice == "6":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main() 