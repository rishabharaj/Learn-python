"""
Lesson 0.2: Running Python

This lesson covers:
1. Using the Python REPL (interactive interpreter)
2. Running Python scripts
3. Understanding Python's execution model
4. Basic command-line usage

To run this script:
1. Run directly: python lesson_0_2_running_python.py
2. Run in interactive mode: python -i lesson_0_2_running_python.py
"""

def demonstrate_repl():
    """Example of what you can do in the Python REPL"""
    print("\nTry these in the Python REPL (interactive interpreter):")
    print("1. Type: 2 + 2")
    print("2. Type: print('Hello, World!')")
    print("3. Type: help() for interactive help")
    print("4. Type: exit() to quit the REPL")

def demonstrate_script_execution():
    """Example of script execution"""
    print("\nScript execution example:")
    print("This message is printed when the script runs")
    
    # Example of command-line arguments
    import sys
    if len(sys.argv) > 1:
        print(f"\nCommand-line arguments: {sys.argv[1:]}")
    else:
        print("\nNo command-line arguments provided")

def main():
    print("Welcome to Python Execution Methods!")
    demonstrate_repl()
    demonstrate_script_execution()
    
    print("\nKey Points:")
    print("1. Python is interpreted, not compiled")
    print("2. You can run code interactively in the REPL")
    print("3. Scripts are executed line by line")
    print("4. Use 'python -m' to run modules as scripts")

if __name__ == "__main__":
    main() 