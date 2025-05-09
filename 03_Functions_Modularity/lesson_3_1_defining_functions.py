"""
Lesson 3.1: Defining Functions

This lesson covers:
1. Function definition and calling
2. Parameters and arguments
3. Return values
4. Docstrings
5. Function scope

Key differences from Java:
- def keyword instead of return type
- No parameter types
- Optional return values
- Docstrings for documentation
- First-class functions
"""

def simple_function():
    """A simple function that prints a message"""
    print("Hello from simple_function!")

def function_with_parameters(name, age):
    """Function with parameters
    
    Args:
        name (str): The person's name
        age (int): The person's age
    """
    print(f"Hello {name}, you are {age} years old!")

def function_with_return(x, y):
    """Function that returns a value
    
    Args:
        x (int): First number
        y (int): Second number
    
    Returns:
        int: The sum of x and y
    """
    return x + y

def function_with_default(name="World"):
    """Function with default parameter
    
    Args:
        name (str, optional): Name to greet. Defaults to "World".
    """
    print(f"Hello, {name}!")

def function_with_docstring():
    """This is a docstring.
    
    It can span multiple lines and should describe:
    - What the function does
    - What parameters it takes
    - What it returns
    - Any exceptions it might raise
    
    Returns:
        str: A greeting message
    """
    return "Hello from a well-documented function!"

def demonstrate_scope():
    """Show function scope examples"""
    print("\nFunction Scope:")
    
    # Global variable
    global_var = "I'm global"
    
    def inner_function():
        # Local variable
        local_var = "I'm local"
        print(f"Inside function: {local_var}")
        print(f"Can access global: {global_var}")
    
    inner_function()
    # print(local_var)  # This would cause an error

def demonstrate_return_values():
    """Show different return value scenarios"""
    print("\nReturn Values:")
    
    def no_return():
        print("This function doesn't return anything")
    
    def return_none():
        print("This function returns None")
        return None
    
    def return_multiple():
        return 1, 2, 3  # Returns a tuple
    
    # Call functions
    result1 = no_return()
    result2 = return_none()
    result3 = return_multiple()
    
    print(f"no_return result: {result1}")
    print(f"return_none result: {result2}")
    print(f"return_multiple result: {result3}")

def main():
    print("Welcome to Python Functions!")
    
    # Call simple function
    simple_function()
    
    # Call function with parameters
    function_with_parameters("Alice", 25)
    
    # Call function with return value
    result = function_with_return(5, 3)
    print(f"Sum: {result}")
    
    # Call function with default parameter
    function_with_default()
    function_with_default("Python")
    
    # Show docstring
    print("\nFunction Docstring:")
    print(function_with_docstring.__doc__)
    
    # Demonstrate scope
    demonstrate_scope()
    
    # Demonstrate return values
    demonstrate_return_values()
    
    print("\nKey Points:")
    print("1. Functions are defined with def")
    print("2. Parameters can have default values")
    print("3. Functions can return multiple values (as tuples)")
    print("4. Docstrings document functions")
    print("5. Variables have function scope")

if __name__ == "__main__":
    main() 