"""
Lesson 8.1: Virtual Environments and pip

This lesson covers:
- Creating and managing virtual environments
- Using pip for package management
- Requirements files
"""

import os
import subprocess
import sys
from typing import List

def create_venv(venv_name: str) -> None:
    """Create a new virtual environment"""
    try:
        subprocess.run([sys.executable, "-m", "venv", venv_name], check=True)
        print(f"Created virtual environment: {venv_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")

def install_packages(packages: List[str]) -> None:
    """Install packages using pip"""
    try:
        subprocess.run([sys.executable, "-m", "pip", "install"] + packages, check=True)
        print(f"Installed packages: {', '.join(packages)}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")

def create_requirements_file(packages: List[str], filename: str = "requirements.txt") -> None:
    """Create a requirements.txt file"""
    try:
        with open(filename, "w") as f:
            for package in packages:
                f.write(f"{package}\n")
        print(f"Created requirements file: {filename}")
    except IOError as e:
        print(f"Error creating requirements file: {e}")

def main():
    """Main function to demonstrate virtual environments and pip"""
    # Example packages to install
    example_packages = ["requests", "python-dotenv", "rich"]
    
    # Create a virtual environment
    venv_name = "my_venv"
    create_venv(venv_name)
    
    # Install packages
    install_packages(example_packages)
    
    # Create requirements file
    create_requirements_file(example_packages)
    
    print("\nTo activate the virtual environment:")
    if sys.platform == "win32":
        print(f"  {venv_name}\\Scripts\\activate")
    else:
        print(f"  source {venv_name}/bin/activate")
    
    print("\nTo deactivate the virtual environment:")
    print("  deactivate")

if __name__ == "__main__":
    main() 