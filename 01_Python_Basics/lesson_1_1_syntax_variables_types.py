"""
Lesson 1.1: Syntax, Variables & Types

This lesson covers:
1. Python's indentation-based syntax
2. Variable assignment and dynamic typing
3. Basic built-in types
4. Type checking and conversion

Key differences from Java:
- No semicolons needed
- No braces for blocks (uses indentation)
- Dynamic typing (no type declarations)
- No need for main() method
"""

def demonstrate_syntax():
    """Show basic Python syntax"""
    print("\nBasic Syntax Examples:")
    
    # Indentation-based blocks
    if True:
        print("This is inside an if block")
        print("Indentation matters!")
    
    # No braces needed
    for i in range(3):
        print(f"Loop iteration {i}")

def demonstrate_variables():
    """Show variable assignment and types"""
    print("\nVariable Examples:")
    
    # Dynamic typing
    x = 10          # integer
    y = 3.14        # float
    z = "Hello"     # string
    flag = True     # boolean
    nothing = None  # None type
    
    print(f"x is {x} (type: {type(x)})")
    print(f"y is {y} (type: {type(y)})")
    print(f"z is {z} (type: {type(z)})")
    print(f"flag is {flag} (type: {type(flag)})")
    print(f"nothing is {nothing} (type: {type(nothing)})")

def demonstrate_type_conversion():
    """Show type conversion examples"""
    print("\nType Conversion Examples:")
    
    # Converting between types
    num_str = "123"
    num_int = int(num_str)
    num_float = float(num_str)
    
    print(f"String to int: {num_str} -> {num_int}")
    print(f"String to float: {num_str} -> {num_float}")
    
    # Converting back to string
    back_to_str = str(num_int)
    print(f"Int back to string: {num_int} -> {back_to_str}")

def main():
    print("Welcome to Python Syntax and Types!")
    demonstrate_syntax()
    demonstrate_variables()
    demonstrate_type_conversion()
    
    print("\nKey Points:")
    print("1. Python uses indentation for code blocks")
    print("2. Variables are dynamically typed")
    print("3. Common types: int, float, str, bool, None")
    print("4. Use type() to check variable types")
    print("5. Use int(), float(), str() for type conversion")

if __name__ == "__main__":
    main() 