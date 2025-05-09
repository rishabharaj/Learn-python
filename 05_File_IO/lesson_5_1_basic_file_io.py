"""
Lesson 5.1: Basic File I/O

This lesson covers:
1. Opening and closing files
2. Reading files
3. Writing files
4. File modes
5. Context managers

Key differences from Java:
- No need for explicit file streams
- Context managers (with statement) for automatic cleanup
- Simpler file operations
- Built-in file object methods
"""

import os
from typing import List

def demonstrate_file_creation():
    """Show how to create and write to files"""
    print("\nFile Creation Examples:")
    
    # Write to a file
    with open("example.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")
        file.write("Python file I/O is simple!\n")
    
    print("Created example.txt")

def demonstrate_file_reading():
    """Show different ways to read files"""
    print("\nFile Reading Examples:")
    
    # Read entire file
    with open("example.txt", "r") as file:
        content = file.read()
        print("\nEntire file content:")
        print(content)
    
    # Read line by line
    with open("example.txt", "r") as file:
        print("\nLine by line:")
        for line in file:
            print(f"Line: {line.strip()}")
    
    # Read lines into list
    with open("example.txt", "r") as file:
        lines: List[str] = file.readlines()
        print("\nLines as list:")
        for i, line in enumerate(lines, 1):
            print(f"Line {i}: {line.strip()}")

def demonstrate_file_appending():
    """Show how to append to files"""
    print("\nFile Appending Examples:")
    
    # Append to file
    with open("example.txt", "a") as file:
        file.write("This line was appended.\n")
    
    print("Appended to example.txt")
    
    # Show updated content
    with open("example.txt", "r") as file:
        print("\nUpdated content:")
        print(file.read())

def demonstrate_file_modes():
    """Show different file modes"""
    print("\nFile Mode Examples:")
    
    # Create a new file
    with open("new_file.txt", "x") as file:
        file.write("This is a new file.\n")
    
    print("Created new_file.txt with 'x' mode")
    
    # Read and write
    with open("new_file.txt", "r+") as file:
        content = file.read()
        print(f"Current content: {content}")
        file.write("Added with r+ mode.\n")
    
    print("Updated new_file.txt with 'r+' mode")

def demonstrate_context_managers():
    """Show the benefits of context managers"""
    print("\nContext Manager Examples:")
    
    # Without context manager
    file = open("temp.txt", "w")
    try:
        file.write("This is a temporary file.\n")
    finally:
        file.close()
    
    print("Created temp.txt without context manager")
    
    # With context manager (preferred)
    with open("temp.txt", "a") as file:
        file.write("Added with context manager.\n")
    
    print("Updated temp.txt with context manager")

def demonstrate_file_operations():
    """Show common file operations"""
    print("\nFile Operations Examples:")
    
    # Check if file exists
    exists = os.path.exists("example.txt")
    print(f"example.txt exists: {exists}")
    
    # Get file size
    size = os.path.getsize("example.txt")
    print(f"example.txt size: {size} bytes")
    
    # Rename file
    os.rename("temp.txt", "renamed.txt")
    print("Renamed temp.txt to renamed.txt")
    
    # Delete file
    os.remove("renamed.txt")
    print("Deleted renamed.txt")

def main():
    print("Welcome to Python File I/O!")
    demonstrate_file_creation()
    demonstrate_file_reading()
    demonstrate_file_appending()
    demonstrate_file_modes()
    demonstrate_context_managers()
    demonstrate_file_operations()
    
    print("\nKey Points:")
    print("1. Use 'with' statement for automatic file cleanup")
    print("2. Different file modes for different operations")
    print("3. Files can be read all at once or line by line")
    print("4. os module provides file operations")
    print("5. Always handle file operations safely")

if __name__ == "__main__":
    main() 