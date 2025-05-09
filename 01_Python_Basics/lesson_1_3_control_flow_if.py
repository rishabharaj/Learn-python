"""
Lesson 1.3: Control Flow - Conditionals

This lesson covers:
1. if, elif, else statements
2. Truthiness in Python
3. Nested conditionals
4. Ternary operator

Key differences from Java:
- No parentheses around conditions (optional)
- elif instead of else if
- Truthiness based on object's __bool__ or __len__
- Ternary operator uses different syntax
"""

def demonstrate_basic_if():
    """Show basic if statement examples"""
    print("\nBasic if Statements:")
    
    age = 18
    
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")

def demonstrate_elif():
    """Show elif usage"""
    print("\nif-elif-else Statements:")
    
    grade = 85
    
    if grade >= 90:
        print("Grade: A")
    elif grade >= 80:
        print("Grade: B")
    elif grade >= 70:
        print("Grade: C")
    elif grade >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

def demonstrate_truthiness():
    """Show Python's truthiness concept"""
    print("\nTruthiness Examples:")
    
    # False values
    false_values = [False, None, 0, "", [], (), {}]
    for value in false_values:
        print(f"{value} is {bool(value)}")
    
    # True values
    true_values = [True, 1, "hello", [1], (1,), {"key": "value"}]
    for value in true_values:
        print(f"{value} is {bool(value)}")

def demonstrate_nested_conditionals():
    """Show nested if statements"""
    print("\nNested Conditionals:")
    
    age = 25
    has_license = True
    
    if age >= 18:
        if has_license:
            print("You can drive")
        else:
            print("You need a license to drive")
    else:
        print("You're too young to drive")

def demonstrate_ternary():
    """Show ternary operator usage"""
    print("\nTernary Operator:")
    
    age = 20
    status = "adult" if age >= 18 else "minor"
    print(f"Age {age}: {status}")

def main():
    print("Welcome to Python Control Flow - Conditionals!")
    demonstrate_basic_if()
    demonstrate_elif()
    demonstrate_truthiness()
    demonstrate_nested_conditionals()
    demonstrate_ternary()
    
    print("\nKey Points:")
    print("1. if, elif, else statements control program flow")
    print("2. Conditions don't need parentheses (but can have them)")
    print("3. Python has truthiness - values can be True or False")
    print("4. Ternary operator: x if condition else y")
    print("5. Nested conditionals are allowed but should be used carefully")

if __name__ == "__main__":
    main() 