"""
Lesson 7.2: Task Manager with Timestamps and Enhanced Features

This version of the task manager includes:
- Timestamps for task creation and completion
- File path configuration via command line arguments
- Enhanced task display with dates
"""

import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Any

class Task:
    """Represents a task with timestamps"""
    
    def __init__(self, description: str):
        self.description = description
        self.created_at = datetime.now()
        self.completed_at = None
        self.is_completed = False
    
    def complete(self) -> None:
        """Mark the task as completed"""
        self.is_completed = True
        self.completed_at = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary for JSON serialization"""
        return {
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "is_completed": self.is_completed
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """Create task from dictionary"""
        task = cls(data["description"])
        task.created_at = datetime.fromisoformat(data["created_at"])
        if data["completed_at"]:
            task.completed_at = datetime.fromisoformat(data["completed_at"])
        task.is_completed = data["is_completed"]
        return task
    
    def __str__(self) -> str:
        """String representation of the task"""
        status = "✓" if self.is_completed else "✗"
        created = self.created_at.strftime("%Y-%m-%d %H:%M")
        completed = self.completed_at.strftime("%Y-%m-%d %H:%M") if self.completed_at else "Not completed"
        return f"{status} {self.description} (Created: {created}, Completed: {completed})"

class TaskManager:
    """Manages a list of tasks with file persistence"""
    
    def __init__(self, data_file: str = "tasks.json"):
        self.data_file = data_file
        self.tasks: List[Task] = []
        self.load_tasks()
    
    def load_tasks(self) -> None:
        """Load tasks from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []
    
    def save_tasks(self) -> None:
        """Save tasks to file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, description: str) -> None:
        """Add a new task"""
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Added task: {description}")
    
    def complete_task(self, index: int) -> None:
        """Mark a task as completed"""
        try:
            task = self.tasks[index]
            task.complete()
            self.save_tasks()
            print(f"Completed task: {task.description}")
        except IndexError:
            print("Invalid task index")
    
    def list_tasks(self) -> None:
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found")
            return
        
        print("\nTasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

def main():
    """Main function"""
    # Get data file from command line arguments or use default
    data_file = sys.argv[1] if len(sys.argv) > 1 else "tasks.json"
    manager = TaskManager(data_file)
    
    while True:
        print("\nTask Manager Menu:")
        print("1. Add task")
        print("2. Complete task")
        print("3. List tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            description = input("Enter task description: ")
            manager.add_task(description)
        elif choice == "2":
            manager.list_tasks()
            try:
                index = int(input("Enter task number to complete: ")) - 1
                manager.complete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            manager.list_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 