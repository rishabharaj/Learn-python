"""
Lesson 2.1: Lists and Tuples

This lesson covers:
1. Lists (mutable sequences)
2. Tuples (immutable sequences)
3. Common operations
4. Slicing and indexing
5. List methods

Key differences from Java:
- Lists are like ArrayList but more flexible
- Tuples are immutable lists
- Negative indexing
- Slicing syntax
- List comprehensions
"""

def demonstrate_lists():
    """Show list examples"""
    print("\nLists:")
    
    # Creating lists
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    empty = []
    
    print(f"Numbers: {numbers}")
    print(f"Mixed: {mixed}")
    print(f"Empty: {empty}")
    
    # List operations
    print("\nList Operations:")
    numbers.append(6)  # Add to end
    print(f"After append: {numbers}")
    
    numbers.insert(0, 0)  # Insert at index
    print(f"After insert: {numbers}")
    
    numbers.remove(3)  # Remove first occurrence
    print(f"After remove: {numbers}")
    
    popped = numbers.pop()  # Remove and return last item
    print(f"Popped: {popped}")
    print(f"After pop: {numbers}")

def demonstrate_indexing():
    """Show indexing and slicing"""
    print("\nIndexing and Slicing:")
    
    numbers = [0, 1, 2, 3, 4, 5]
    
    # Positive indexing
    print(f"First element: {numbers[0]}")
    print(f"Last element: {numbers[-1]}")
    
    # Slicing
    print(f"First three: {numbers[:3]}")
    print(f"Last three: {numbers[-3:]}")
    print(f"Middle: {numbers[2:4]}")
    print(f"Every other: {numbers[::2]}")

def demonstrate_tuples():
    """Show tuple examples"""
    print("\nTuples:")
    
    # Creating tuples
    point = (3, 4)
    single = (1,)  # Note the comma
    empty = ()
    
    print(f"Point: {point}")
    print(f"Single: {single}")
    print(f"Empty: {empty}")
    
    # Tuple operations
    print("\nTuple Operations:")
    x, y = point  # Unpacking
    print(f"x: {x}, y: {y}")
    
    # Tuples are immutable
    try:
        point[0] = 5
    except TypeError as e:
        print(f"Cannot modify tuple: {e}")

def demonstrate_list_methods():
    """Show common list methods"""
    print("\nList Methods:")
    
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"Original: {numbers}")
    
    # Sorting
    numbers.sort()
    print(f"Sorted: {numbers}")
    
    # Reversing
    numbers.reverse()
    print(f"Reversed: {numbers}")
    
    # Counting
    count = numbers.count(5)
    print(f"Count of 5: {count}")
    
    # Copying
    copy = numbers.copy()
    print(f"Copy: {copy}")

def main():
    print("Welcome to Python Lists and Tuples!")
    demonstrate_lists()
    demonstrate_indexing()
    demonstrate_tuples()
    demonstrate_list_methods()
    
    print("\nKey Points:")
    print("1. Lists are mutable, tuples are immutable")
    print("2. Lists use square brackets [], tuples use parentheses ()")
    print("3. Negative indices count from the end")
    print("4. Slicing: [start:stop:step]")
    print("5. Lists have many useful methods (append, insert, remove, etc.)")

if __name__ == "__main__":
    main() 