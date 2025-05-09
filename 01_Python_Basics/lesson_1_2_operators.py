"""
Lesson 1.2: Operators

This lesson covers:
1. Arithmetic operators
2. Comparison operators
3. Logical operators
4. Assignment operators
5. Membership and identity operators

Key differences from Java:
- No ++ or -- operators
- Different division operators (/ and //)
- ** for exponentiation
- is and is not for identity comparison
"""

def demonstrate_arithmetic_operators():
    """Show arithmetic operator examples"""
    print("\nArithmetic Operators:")
    
    a = 10
    b = 3
    
    print(f"{a} + {b} = {a + b}")  # Addition
    print(f"{a} - {b} = {a - b}")  # Subtraction
    print(f"{a} * {b} = {a * b}")  # Multiplication
    print(f"{a} / {b} = {a / b}")  # Division (float)
    print(f"{a} // {b} = {a // b}") # Floor division
    print(f"{a} % {b} = {a % b}")  # Modulus
    print(f"{a} ** {b} = {a ** b}") # Exponentiation

def demonstrate_comparison_operators():
    """Show comparison operator examples"""
    print("\nComparison Operators:")
    
    x = 5
    y = 10
    
    print(f"{x} == {y}: {x == y}")  # Equal to
    print(f"{x} != {y}: {x != y}")  # Not equal to
    print(f"{x} > {y}: {x > y}")    # Greater than
    print(f"{x} < {y}: {x < y}")    # Less than
    print(f"{x} >= {y}: {x >= y}")  # Greater than or equal to
    print(f"{x} <= {y}: {x <= y}")  # Less than or equal to

def demonstrate_logical_operators():
    """Show logical operator examples"""
    print("\nLogical Operators:")
    
    a = True
    b = False
    
    print(f"{a} and {b}: {a and b}")  # AND
    print(f"{a} or {b}: {a or b}")    # OR
    print(f"not {a}: {not a}")        # NOT

def demonstrate_membership_operators():
    """Show membership operator examples"""
    print("\nMembership Operators:")
    
    fruits = ["apple", "banana", "cherry"]
    
    print(f"'apple' in {fruits}: {'apple' in fruits}")
    print(f"'orange' not in {fruits}: {'orange' not in fruits}")

def demonstrate_identity_operators():
    """Show identity operator examples"""
    print("\nIdentity Operators:")
    
    x = [1, 2, 3]
    y = [1, 2, 3]
    z = x
    
    print(f"x is z: {x is z}")      # True, same object
    print(f"x is y: {x is y}")      # False, different objects
    print(f"x == y: {x == y}")      # True, same values

def main():
    print("Welcome to Python Operators!")
    demonstrate_arithmetic_operators()
    demonstrate_comparison_operators()
    demonstrate_logical_operators()
    demonstrate_membership_operators()
    demonstrate_identity_operators()
    
    print("\nKey Points:")
    print("1. / gives float division, // gives integer division")
    print("2. ** is used for exponentiation")
    print("3. is compares object identity, == compares values")
    print("4. in and not in check membership in sequences")
    print("5. and, or, not are logical operators")

if __name__ == "__main__":
    main() 