"""
Lesson 0.1: Environment Setup

This lesson covers:
1. Installing Python
2. Verifying the installation
3. Setting up VS Code with Python extension
4. Basic environment configuration

To run this script:
1. Make sure Python is installed (python --version)
2. Run this file using: python lesson_0_1_environment.py
"""

def main():
    print("Welcome to Python Learning!")
    print("\nEnvironment Setup Instructions:")
    print("1. Install Python from python.org")
    print("2. Verify installation by running 'python --version'")
    print("3. Install VS Code and the Python extension")
    print("4. Configure your environment variables if needed")
    
    # Basic Python version check
    import sys
    print(f"\nYour Python version: {sys.version}")
    
    # Check if we're in a virtual environment
    import sys
    print(f"Running in virtual environment: {hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)}")

if __name__ == "__main__":
    main() 