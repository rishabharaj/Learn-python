"""
Lesson 7.1: Standard Library Essentials - datetime, os, sys

This lesson covers essential Python standard library modules:
- datetime: Working with dates and times
- os: Operating system interface
- sys: System-specific parameters and functions
"""

import datetime
import os
import sys

def datetime_examples():
    """Examples of using the datetime module"""
    # Current date and time
    now = datetime.datetime.now()
    print(f"Current date and time: {now}")
    
    # Creating specific dates
    birthday = datetime.date(1990, 1, 1)
    print(f"Birthday: {birthday}")
    
    # Time differences
    delta = datetime.timedelta(days=7)
    next_week = now + delta
    print(f"Next week: {next_week}")
    
    # Formatting dates
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Formatted date: {formatted}")

def os_examples():
    """Examples of using the os module"""
    # Current working directory
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")
    
    # List directory contents
    print("\nDirectory contents:")
    for item in os.listdir(cwd):
        print(f"- {item}")
    
    # Check if path exists
    path = "example.txt"
    exists = os.path.exists(path)
    print(f"\nDoes {path} exist? {exists}")
    
    # Create directory
    new_dir = "test_dir"
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print(f"Created directory: {new_dir}")

def sys_examples():
    """Examples of using the sys module"""
    # Command line arguments
    print(f"Script name: {sys.argv[0]}")
    print(f"Arguments: {sys.argv[1:]}")
    
    # Python version
    print(f"Python version: {sys.version}")
    
    # System path
    print("\nPython path:")
    for path in sys.path:
        print(f"- {path}")

def main():
    """Main function to demonstrate all examples"""
    print("=== datetime Examples ===")
    datetime_examples()
    
    print("\n=== os Examples ===")
    os_examples()
    
    print("\n=== sys Examples ===")
    sys_examples()

if __name__ == "__main__":
    main() 