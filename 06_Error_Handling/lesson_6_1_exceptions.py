"""
Lesson 6.1: Exceptions and Error Handling

This lesson covers:
1. Exception types
2. Try-except blocks
3. Raising exceptions
4. Custom exceptions
5. Exception handling best practices

Key differences from Java:
- No checked exceptions
- Simpler exception hierarchy
- More flexible exception handling
- Context managers for cleanup
"""

from typing import Optional

def demonstrate_basic_exceptions():
    """Show basic exception handling"""
    print("\nBasic Exception Examples:")
    
    # Division by zero
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    
    # Index out of range
    try:
        numbers = [1, 2, 3]
        print(numbers[5])
    except IndexError as e:
        print(f"Caught IndexError: {e}")
    
    # Key error
    try:
        d = {"a": 1, "b": 2}
        print(d["c"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")

def demonstrate_multiple_exceptions():
    """Show handling multiple exceptions"""
    print("\nMultiple Exception Examples:")
    
    def divide(a: int, b: int) -> float:
        """Divide two numbers
        
        Args:
            a: The numerator
            b: The denominator
            
        Returns:
            The result of division
            
        Raises:
            ZeroDivisionError: If b is zero
            TypeError: If a or b are not numbers
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a / b
    
    # Test different cases
    test_cases = [
        (10, 2),    # Valid
        (10, 0),    # Division by zero
        ("10", 2),  # Type error
    ]
    
    for a, b in test_cases:
        try:
            result = divide(a, b)
            print(f"{a} / {b} = {result}")
        except ZeroDivisionError:
            print(f"Cannot divide {a} by zero")
        except TypeError as e:
            print(f"Type error: {e}")

def demonstrate_custom_exceptions():
    """Show custom exception usage"""
    print("\nCustom Exception Examples:")
    
    class ValidationError(Exception):
        """Custom exception for validation errors"""
        pass
    
    class User:
        """A class representing a user"""
        
        def __init__(self, username: str, age: int):
            """Initialize a new user
            
            Args:
                username: The user's username
                age: The user's age
                
            Raises:
                ValidationError: If validation fails
            """
            if not username:
                raise ValidationError("Username cannot be empty")
            if age < 0:
                raise ValidationError("Age cannot be negative")
            
            self.username = username
            self.age = age
    
    # Test user creation
    test_cases = [
        ("john", 25),      # Valid
        ("", 25),          # Empty username
        ("john", -5),      # Negative age
    ]
    
    for username, age in test_cases:
        try:
            user = User(username, age)
            print(f"Created user: {user.username}, age {user.age}")
        except ValidationError as e:
            print(f"Validation error: {e}")

def demonstrate_exception_chain():
    """Show exception chaining"""
    print("\nException Chaining Examples:")
    
    def process_data(data: Optional[dict]) -> None:
        """Process some data
        
        Args:
            data: The data to process
            
        Raises:
            ValueError: If data is invalid
        """
        if not data:
            raise ValueError("No data provided")
        
        try:
            value = data["key"]
            result = 10 / value
        except KeyError as e:
            raise ValueError("Missing required key") from e
        except ZeroDivisionError as e:
            raise ValueError("Invalid value: division by zero") from e
    
    # Test different cases
    test_cases = [
        {"key": 2},    # Valid
        {},            # Missing key
        {"key": 0},    # Division by zero
        None,          # No data
    ]
    
    for data in test_cases:
        try:
            process_data(data)
            print("Data processed successfully")
        except ValueError as e:
            print(f"Error: {e}")
            if e.__cause__:
                print(f"Caused by: {e.__cause__}")

def demonstrate_finally():
    """Show finally block usage"""
    print("\nFinally Block Examples:")
    
    def process_file(filename: str) -> None:
        """Process a file
        
        Args:
            filename: The name of the file to process
        """
        file = None
        try:
            file = open(filename, "r")
            content = file.read()
            print(f"File content: {content}")
        except FileNotFoundError:
            print(f"File {filename} not found")
        finally:
            if file:
                file.close()
                print("File closed")
    
    # Test file processing
    process_file("example.txt")
    process_file("nonexistent.txt")

def main():
    print("Welcome to Python Exception Handling!")
    demonstrate_basic_exceptions()
    demonstrate_multiple_exceptions()
    demonstrate_custom_exceptions()
    demonstrate_exception_chain()
    demonstrate_finally()
    
    print("\nKey Points:")
    print("1. Use try-except blocks for error handling")
    print("2. Handle specific exceptions when possible")
    print("3. Create custom exceptions for domain-specific errors")
    print("4. Use finally for cleanup operations")
    print("5. Chain exceptions to preserve context")

if __name__ == "__main__":
    main() 