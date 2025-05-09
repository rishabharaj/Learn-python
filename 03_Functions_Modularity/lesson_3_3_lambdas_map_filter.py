"""
Lesson 3.3: Lambdas and Functional Programming

This lesson covers:
1. Lambda functions
2. map() function
3. filter() function
4. List comprehensions
5. Functional programming concepts

Key differences from Java:
- Lambda syntax is more concise
- Functions are first-class citizens
- No need for functional interfaces
- Built-in map and filter functions
- List comprehensions as an alternative
"""

def demonstrate_lambdas():
    """Show lambda function examples"""
    print("\nLambda Functions:")
    
    # Simple lambda
    square = lambda x: x ** 2
    print(f"Square of 5: {square(5)}")
    
    # Lambda with multiple arguments
    add = lambda x, y: x + y
    print(f"Add 3 and 4: {add(3, 4)}")
    
    # Lambda in sorting
    points = [(1, 2), (3, 1), (5, 4)]
    sorted_points = sorted(points, key=lambda p: p[1])
    print(f"Sorted points: {sorted_points}")

def demonstrate_map():
    """Show map function examples"""
    print("\nMap Function:")
    
    # Basic map
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x ** 2, numbers))
    print(f"Squares: {squares}")
    
    # Map with multiple iterables
    a = [1, 2, 3]
    b = [4, 5, 6]
    sums = list(map(lambda x, y: x + y, a, b))
    print(f"Sums: {sums}")
    
    # Map vs list comprehension
    squares_lc = [x ** 2 for x in numbers]
    print(f"Squares (list comp): {squares_lc}")

def demonstrate_filter():
    """Show filter function examples"""
    print("\nFilter Function:")
    
    # Basic filter
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")
    
    # Filter with None
    values = [0, 1, "", "hello", None, True, False]
    truthy = list(filter(None, values))
    print(f"Truthy values: {truthy}")
    
    # Filter vs list comprehension
    evens_lc = [x for x in numbers if x % 2 == 0]
    print(f"Even numbers (list comp): {evens_lc}")

def demonstrate_functional_concepts():
    """Show functional programming concepts"""
    print("\nFunctional Programming Concepts:")
    
    # Higher-order functions
    def apply_operation(func, x, y):
        return func(x, y)
    
    result = apply_operation(lambda a, b: a * b, 3, 4)
    print(f"Apply operation result: {result}")
    
    # Function composition
    def compose(f, g):
        return lambda x: f(g(x))
    
    double = lambda x: x * 2
    square = lambda x: x ** 2
    double_then_square = compose(square, double)
    print(f"Double then square 3: {double_then_square(3)}")

def demonstrate_list_comprehensions():
    """Show list comprehension examples"""
    print("\nList Comprehensions:")
    
    # Basic list comprehension
    squares = [x ** 2 for x in range(5)]
    print(f"Squares: {squares}")
    
    # List comprehension with condition
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"Evens: {evens}")
    
    # Nested list comprehension
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"Flattened matrix: {flattened}")

def main():
    print("Welcome to Python Functional Programming!")
    demonstrate_lambdas()
    demonstrate_map()
    demonstrate_filter()
    demonstrate_functional_concepts()
    demonstrate_list_comprehensions()
    
    print("\nKey Points:")
    print("1. Lambdas are anonymous functions")
    print("2. map() applies a function to all items")
    print("3. filter() selects items based on a condition")
    print("4. List comprehensions are often more readable")
    print("5. Functions are first-class citizens in Python")

if __name__ == "__main__":
    main() 