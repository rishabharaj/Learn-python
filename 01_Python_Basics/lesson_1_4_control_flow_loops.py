"""
Lesson 1.4: Control Flow - Loops

This lesson covers:
1. for loops
2. while loops
3. break and continue
4. else clause in loops
5. range() function

Key differences from Java:
- for loops iterate over sequences
- while loops are similar but with different syntax
- else clause can be used with loops
- range() function for numeric sequences
"""

def demonstrate_for_loops():
    """Show for loop examples"""
    print("\nFor Loops:")
    
    # Iterating over a list
    fruits = ["apple", "banana", "cherry"]
    print("Iterating over a list:")
    for fruit in fruits:
        print(fruit)
    
    # Using range()
    print("\nUsing range():")
    for i in range(5):  # 0 to 4
        print(i)
    
    # range() with start and step
    print("\nrange() with start and step:")
    for i in range(2, 10, 2):  # start at 2, step by 2, up to 10
        print(i)

def demonstrate_while_loops():
    """Show while loop examples"""
    print("\nWhile Loops:")
    
    # Basic while loop
    count = 0
    while count < 5:
        print(f"Count: {count}")
        count += 1
    
    # While with break
    print("\nWhile with break:")
    count = 0
    while True:
        if count >= 5:
            break
        print(f"Count: {count}")
        count += 1

def demonstrate_break_continue():
    """Show break and continue usage"""
    print("\nBreak and Continue:")
    
    # break example
    print("Break example:")
    for i in range(10):
        if i == 5:
            break
        print(i)
    
    # continue example
    print("\nContinue example:")
    for i in range(5):
        if i == 2:
            continue
        print(i)

def demonstrate_else_clause():
    """Show else clause in loops"""
    print("\nElse Clause in Loops:")
    
    # else in for loop
    print("Else in for loop:")
    for i in range(5):
        print(i)
    else:
        print("Loop completed normally")
    
    # else not executed with break
    print("\nElse not executed with break:")
    for i in range(5):
        if i == 3:
            break
        print(i)
    else:
        print("This won't be printed")

def demonstrate_nested_loops():
    """Show nested loop examples"""
    print("\nNested Loops:")
    
    # Multiplication table
    print("Multiplication table:")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i} * {j} = {i * j}", end="\t")
        print()

def main():
    print("Welcome to Python Control Flow - Loops!")
    demonstrate_for_loops()
    demonstrate_while_loops()
    demonstrate_break_continue()
    demonstrate_else_clause()
    demonstrate_nested_loops()
    
    print("\nKey Points:")
    print("1. for loops iterate over sequences")
    print("2. while loops repeat while condition is true")
    print("3. break exits the loop, continue skips to next iteration")
    print("4. else clause executes if loop completes normally")
    print("5. range() generates numeric sequences")

if __name__ == "__main__":
    main() 