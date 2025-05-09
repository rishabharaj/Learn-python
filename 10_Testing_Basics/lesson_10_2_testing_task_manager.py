"""
Lesson 10.2: Testing Task Manager

This lesson covers:
- Writing test cases for the task manager
- Mocking dependencies
- Testing file operations
- Testing error handling
- Test coverage
"""

import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
from datetime import datetime
from typing import Dict, Any

# Import the task manager classes
class Task:
    """Task class for testing"""
    
    def __init__(self, description: str):
        self.description = description
        self.created_at = datetime.now()
        self.completed_at = None
        self.is_completed = False
    
    def complete(self) -> None:
        self.is_completed = True
        self.completed_at = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "is_completed": self.is_completed
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        task = cls(data["description"])
        task.created_at = datetime.fromisoformat(data["created_at"])
        if data["completed_at"]:
            task.completed_at = datetime.fromisoformat(data["completed_at"])
        task.is_completed = data["is_completed"]
        return task

class TaskManager:
    """Task manager class for testing"""
    
    def __init__(self, data_file: str = "tasks.json"):
        self.data_file = data_file
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self) -> None:
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []
    
    def save_tasks(self) -> None:
        with open(self.data_file, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2)
    
    def add_task(self, description: str) -> None:
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()
    
    def complete_task(self, index: int) -> None:
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()
            self.save_tasks()

# Test cases
class TestTask(unittest.TestCase):
    """Test cases for Task class"""
    
    def setUp(self) -> None:
        self.task = Task("Test task")
    
    def test_task_creation(self) -> None:
        self.assertEqual(self.task.description, "Test task")
        self.assertFalse(self.task.is_completed)
        self.assertIsNone(self.task.completed_at)
    
    def test_task_completion(self) -> None:
        self.task.complete()
        self.assertTrue(self.task.is_completed)
        self.assertIsNotNone(self.task.completed_at)
    
    def test_task_serialization(self) -> None:
        task_dict = self.task.to_dict()
        self.assertIn("description", task_dict)
        self.assertIn("created_at", task_dict)
        self.assertIn("completed_at", task_dict)
        self.assertIn("is_completed", task_dict)

class TestTaskManager(unittest.TestCase):
    """Test cases for TaskManager class"""
    
    def setUp(self) -> None:
        self.manager = TaskManager("test_tasks.json")
    
    @patch("builtins.open", new_callable=mock_open)
    def test_load_tasks(self, mock_file: MagicMock) -> None:
        # Mock JSON data
        mock_data = [
            {
                "description": "Test task",
                "created_at": datetime.now().isoformat(),
                "completed_at": None,
                "is_completed": False
            }
        ]
        mock_file.return_value.__enter__.return_value.read.return_value = json.dumps(mock_data)
        
        # Test loading tasks
        self.manager.load_tasks()
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].description, "Test task")
    
    @patch("builtins.open", new_callable=mock_open)
    def test_save_tasks(self, mock_file: MagicMock) -> None:
        # Add a task
        self.manager.add_task("Test task")
        
        # Verify file was opened for writing
        mock_file.assert_called_once_with("test_tasks.json", 'w')
    
    def test_add_task(self) -> None:
        self.manager.add_task("New task")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].description, "New task")
    
    def test_complete_task(self) -> None:
        self.manager.add_task("Task to complete")
        self.manager.complete_task(0)
        self.assertTrue(self.manager.tasks[0].is_completed)
    
    def test_complete_task_invalid_index(self) -> None:
        # Should not raise an exception for invalid index
        self.manager.complete_task(999)

def main() -> None:
    """Main function to run tests"""
    unittest.main(argv=[''], exit=False)

if __name__ == "__main__":
    main() 