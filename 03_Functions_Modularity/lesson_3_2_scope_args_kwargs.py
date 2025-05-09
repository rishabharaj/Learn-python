"""
Lesson 3.2: Scope and Arguments

This lesson covers:
1. Variable scope (local, global, nonlocal)
2. Positional and keyword arguments
3. Variable-length arguments (*args, **kwargs)
4. Argument unpacking
5. Function annotations

Key differences from Java:
- No method overloading
- Variable number of arguments
- Keyword arguments
- Argument unpacking
- Function annotations (type hints)
"""

def demonstrate_scope():
    """Show different types of variable scope"""
    print("\nVariable Scope:")
    
    # Global variable
    global_var = "I'm global"
    
    def outer_function():
        # Nonlocal variable
        nonlocal_var = "I'm nonlocal"
        
        def inner_function():
            # Local variable
            local_var = "I'm local"
            print(f"Inside inner: {local_var}")
            print(f"Can access nonlocal: {nonlocal_var}")
            print(f"Can access global: {global_var}")
        
        inner_function()
        print(f"Inside outer: {nonlocal_var}")
    
    outer_function()
    print(f"Global scope: {global_var}")

def demonstrate_global_keyword():
    """Show how to modify global variables"""
    print("\nGlobal Keyword:")
    
    counter = 0
    
    def increment_counter():
        global counter
        counter += 1
        print(f"Counter: {counter}")
    
    increment_counter()
    increment_counter()

def demonstrate_args_kwargs():
    """Show variable-length arguments"""
    print("\n*args and **kwargs:")
    
    def print_args(*args):
        """Print all positional arguments"""
        print("Positional arguments:")
        for arg in args:
            print(f"- {arg}")
    
    def print_kwargs(**kwargs):
        """Print all keyword arguments"""
        print("Keyword arguments:")
        for key, value in kwargs.items():
            print(f"- {key}: {value}")
    
    def print_all(*args, **kwargs):
        """Print both types of arguments"""
        print_args(*args)
        print_kwargs(**kwargs)
    
    # Call with different arguments
    print_args(1, 2, 3)
    print_kwargs(name="Alice", age=25)
    print_all(1, 2, name="Alice", age=25)

def demonstrate_argument_unpacking():
    """Show how to unpack arguments"""
    print("\nArgument Unpacking:")
    
    def add_numbers(a, b, c):
        return a + b + c
    
    # Unpack list into positional arguments
    numbers = [1, 2, 3]
    result = add_numbers(*numbers)
    print(f"Sum of {numbers}: {result}")
    
    # Unpack dictionary into keyword arguments
    params = {"a": 1, "b": 2, "c": 3}
    result = add_numbers(**params)
    print(f"Sum of {params}: {result}")

def demonstrate_type_annotations():
    """Show function annotations"""
    print("\nType Annotations:")
    
    def greet(name: str, age: int) -> str:
        """Greet someone with their name and age
        
        Args:
            name: The person's name
            age: The person's age
            
        Returns:
            A greeting message
        """
        return f"Hello {name}, you are {age} years old!"
    
    # Call the function
    message = greet("Alice", 25)
    print(message)
    
    # Show annotations
    print("\nFunction annotations:")
    print(greet.__annotations__)

def main():
    print("Welcome to Python Scope and Arguments!")
    demonstrate_scope()
    demonstrate_global_keyword()
    demonstrate_args_kwargs()
    demonstrate_argument_unpacking()
    demonstrate_type_annotations()
    
    print("\nKey Points:")
    print("1. Variables have local, nonlocal, and global scope")
    print("2. *args collects positional arguments")
    print("3. **kwargs collects keyword arguments")
    print("4. Arguments can be unpacked from sequences and mappings")
    print("5. Type annotations provide hints but don't enforce types")

if __name__ == "__main__":
    main() 