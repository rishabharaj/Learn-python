"""
Lesson 9.1: Python Comprehensions

This lesson covers:
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Nested comprehensions
- Generator expressions
"""

from typing import List, Dict, Set, Generator

def list_comprehension_examples() -> None:
    """Examples of list comprehensions"""
    # Basic list comprehension
    numbers = [1, 2, 3, 4, 5]
    squares = [x ** 2 for x in numbers]
    print(f"Squares: {squares}")
    
    # With condition
    evens = [x for x in numbers if x % 2 == 0]
    print(f"Even numbers: {evens}")
    
    # Multiple variables
    pairs = [(x, y) for x in range(3) for y in range(3)]
    print(f"Coordinate pairs: {pairs}")

def dict_comprehension_examples() -> None:
    """Examples of dictionary comprehensions"""
    # Basic dictionary comprehension
    numbers = [1, 2, 3, 4, 5]
    square_dict = {x: x ** 2 for x in numbers}
    print(f"Number squares: {square_dict}")
    
    # With condition
    even_squares = {x: x ** 2 for x in numbers if x % 2 == 0}
    print(f"Even number squares: {even_squares}")
    
    # Swapping keys and values
    swapped = {v: k for k, v in square_dict.items()}
    print(f"Swapped dictionary: {swapped}")

def set_comprehension_examples() -> None:
    """Examples of set comprehensions"""
    # Basic set comprehension
    numbers = [1, 2, 2, 3, 3, 4, 5]
    unique_squares = {x ** 2 for x in numbers}
    print(f"Unique squares: {unique_squares}")
    
    # With condition
    even_squares = {x ** 2 for x in numbers if x % 2 == 0}
    print(f"Even number squares: {even_squares}")

def nested_comprehension_examples() -> None:
    """Examples of nested comprehensions"""
    # Nested list comprehension
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"Flattened matrix: {flattened}")
    
    # Nested dictionary comprehension
    nested_dict = {
        'a': {'x': 1, 'y': 2},
        'b': {'x': 3, 'y': 4}
    }
    flattened_dict = {
        f"{outer_key}_{inner_key}": value
        for outer_key, inner_dict in nested_dict.items()
        for inner_key, value in inner_dict.items()
    }
    print(f"Flattened dictionary: {flattened_dict}")

def generator_expression_examples() -> None:
    """Examples of generator expressions"""
    # Basic generator expression
    numbers = [1, 2, 3, 4, 5]
    squares_gen = (x ** 2 for x in numbers)
    print("Generator squares:", end=" ")
    for square in squares_gen:
        print(square, end=" ")
    print()
    
    # Generator with condition
    even_squares_gen = (x ** 2 for x in numbers if x % 2 == 0)
    print("Even squares:", end=" ")
    for square in even_squares_gen:
        print(square, end=" ")
    print()

def main() -> None:
    """Main function to demonstrate all comprehension types"""
    print("=== List Comprehensions ===")
    list_comprehension_examples()
    
    print("\n=== Dictionary Comprehensions ===")
    dict_comprehension_examples()
    
    print("\n=== Set Comprehensions ===")
    set_comprehension_examples()
    
    print("\n=== Nested Comprehensions ===")
    nested_comprehension_examples()
    
    print("\n=== Generator Expressions ===")
    generator_expression_examples()

if __name__ == "__main__":
    main() 