"""
Lesson 9.3: Decorators and Context Managers

This lesson covers:
- Function decorators
- Class decorators
- Context managers
- with statement
- Resource management
"""

from typing import Callable, Any
import time
from contextlib import contextmanager
import os

# Function decorators
def timer(func: Callable) -> Callable:
    """Decorator to measure function execution time"""
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

def validate_input(func: Callable) -> Callable:
    """Decorator to validate function input"""
    def wrapper(*args, **kwargs) -> Any:
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"Invalid input: {arg} is not a number")
        return func(*args, **kwargs)
    return wrapper

# Class decorator
def singleton(cls: type) -> type:
    """Decorator to make a class a singleton"""
    instances = {}
    
    def get_instance(*args, **kwargs) -> Any:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

# Context manager class
class FileHandler:
    """Context manager for file operations"""
    
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self) -> 'FileHandler':
        self.file = open(self.filename, self.mode)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.file:
            self.file.close()
    
    def write(self, text: str) -> None:
        """Write text to the file"""
        if self.file:
            self.file.write(text)

# Context manager using contextlib
@contextmanager
def temp_file(filename: str) -> Generator[str, None, None]:
    """Context manager for temporary file operations"""
    try:
        with open(filename, 'w') as f:
            yield f
    finally:
        if os.path.exists(filename):
            os.remove(filename)

# Example functions using decorators
@timer
@validate_input
def add_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    time.sleep(1)  # Simulate some work
    return a + b

# Example class using singleton decorator
@singleton
class Database:
    """Example singleton class"""
    
    def __init__(self):
        print("Database connection established")
    
    def query(self, sql: str) -> str:
        """Execute a database query"""
        return f"Executing: {sql}"

def main() -> None:
    """Main function to demonstrate decorators and context managers"""
    # Using function decorators
    print("=== Function Decorators ===")
    result = add_numbers(5, 3)
    print(f"Result: {result}")
    
    try:
        add_numbers("5", 3)  # This will raise ValueError
    except ValueError as e:
        print(f"Error: {e}")
    
    # Using class decorator (singleton)
    print("\n=== Class Decorator (Singleton) ===")
    db1 = Database()
    db2 = Database()
    print(f"Same instance? {db1 is db2}")
    
    # Using context manager class
    print("\n=== Context Manager Class ===")
    with FileHandler("example.txt", "w") as fh:
        fh.write("Hello, World!")
    
    # Using contextlib context manager
    print("\n=== Contextlib Context Manager ===")
    with temp_file("temp.txt") as f:
        f.write("Temporary content")
    print("File deleted after context")

if __name__ == "__main__":
    main() 