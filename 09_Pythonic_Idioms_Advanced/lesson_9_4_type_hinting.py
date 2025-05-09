"""
Lesson 9.4: Type Hinting

This lesson covers:
- Type annotations
- Static type checking
- Type variables
- Generic types
- Type hints in practice
"""

from typing import List, Dict, Optional, Union, TypeVar, Generic, Callable
from dataclasses import dataclass
from datetime import datetime

# Basic type hints
def greet(name: str) -> str:
    """Function with basic type hints"""
    return f"Hello, {name}!"

# Optional and Union types
def process_data(data: Optional[str] = None) -> Union[str, int]:
    """Function with Optional and Union types"""
    if data is None:
        return 0
    return data.upper()

# Type variables and generics
T = TypeVar('T')

class Stack(Generic[T]):
    """Generic stack implementation"""
    
    def __init__(self) -> None:
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        """Push an item onto the stack"""
        self.items.append(item)
    
    def pop(self) -> T:
        """Pop an item from the stack"""
        return self.items.pop()

# Callable type hints
def apply_operation(
    func: Callable[[int, int], int],
    a: int,
    b: int
) -> int:
    """Function with Callable type hint"""
    return func(a, b)

# Dataclass with type hints
@dataclass
class Task:
    """Task class with type hints"""
    description: str
    created_at: datetime
    completed: bool = False
    priority: Optional[int] = None

# Type hints in practice
class TaskManager:
    """Task manager with type hints"""
    
    def __init__(self) -> None:
        self.tasks: Dict[str, Task] = {}
    
    def add_task(self, task: Task) -> None:
        """Add a task to the manager"""
        self.tasks[task.description] = task
    
    def get_task(self, description: str) -> Optional[Task]:
        """Get a task by description"""
        return self.tasks.get(description)
    
    def complete_task(self, description: str) -> bool:
        """Mark a task as completed"""
        task = self.get_task(description)
        if task:
            task.completed = True
            return True
        return False

def main() -> None:
    """Main function to demonstrate type hints"""
    # Basic type hints
    print("=== Basic Type Hints ===")
    message = greet("Python")
    print(message)
    
    # Optional and Union types
    print("\n=== Optional and Union Types ===")
    result1 = process_data()
    result2 = process_data("hello")
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
    
    # Generic types
    print("\n=== Generic Types ===")
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    print(f"Popped: {stack.pop()}")
    
    # Callable type hints
    print("\n=== Callable Type Hints ===")
    def add(a: int, b: int) -> int:
        return a + b
    
    result = apply_operation(add, 5, 3)
    print(f"Result: {result}")
    
    # Dataclass with type hints
    print("\n=== Dataclass with Type Hints ===")
    task = Task(
        description="Learn Python",
        created_at=datetime.now(),
        priority=1
    )
    print(f"Task: {task}")
    
    # Task manager in practice
    print("\n=== Task Manager in Practice ===")
    manager = TaskManager()
    manager.add_task(task)
    found_task = manager.get_task("Learn Python")
    if found_task:
        print(f"Found task: {found_task}")
        manager.complete_task("Learn Python")
        print(f"Task completed: {found_task.completed}")

if __name__ == "__main__":
    main() 