"""
Lesson 5.2: Task Manager File I/O v4

This lesson covers:
1. File-based task persistence
2. JSON serialization
3. Error handling
4. File operations
5. Data validation

This version of the task manager:
- Saves tasks to a JSON file
- Loads tasks on startup
- Handles file errors gracefully
- Validates task data
- Uses context managers
"""

import json
import os
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
    
    def to_dict(self) -> dict:
        """Convert task to dictionary
        
        Returns:
            Dictionary representation of task
        """
        return {
            "type": self.get_type(),
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        """Create task from dictionary
        
        Args:
            data: Dictionary containing task data
            
        Returns:
            Task instance
        """
        task_type = data["type"]
        if task_type == "Basic":
            return BasicTask(data["description"], data["priority"])
        elif task_type == "Timed":
            return TimedTask(
                data["description"],
                datetime.fromisoformat(data["deadline"]),
                data["priority"]
            )
        raise ValueError(f"Unknown task type: {task_type}")
    
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
    
    def to_dict(self) -> dict:
        """Convert task to dictionary
        
        Returns:
            Dictionary representation of task
        """
        data = super().to_dict()
        data["deadline"] = self.deadline.isoformat()
        return data
    
    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str} (Deadline: {self.deadline})"

class TaskManager:
    """A class to manage tasks"""
    
    def __init__(self, filename: str = "tasks.json"):
        """Initialize a new task manager
        
        Args:
            filename: Name of the file to store tasks
        """
        self.filename = filename
        self.tasks: List[Task] = []
        self.load_tasks()
    
    def load_tasks(self) -> None:
        """Load tasks from file"""
        if not os.path.exists(self.filename):
            return
        
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
    
    def save_tasks(self) -> None:
        """Save tasks to file"""
        try:
            with open(self.filename, "w") as file:
                json.dump([task.to_dict() for task in self.tasks], 
                         file, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, task: Task) -> None:
        """Add a new task
        
        Args:
            task: The task to add
        """
        self.tasks.append(task)
        self.save_tasks()
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
            self.save_tasks()
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
    print("\nTask Manager v4")
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