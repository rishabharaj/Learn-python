"""
Lesson 2.2: Dictionaries and Sets

This lesson covers:
1. Dictionaries (key-value pairs)
2. Sets (unique collections)
3. Common operations
4. Dictionary methods
5. Set operations

Key differences from Java:
- Dictionaries are like HashMaps but more flexible
- Sets are like HashSet but with more operations
- Dictionary comprehensions
- Set comprehensions
- Default values in dictionaries
"""

def demonstrate_dictionaries():
    """Show dictionary examples"""
    print("\nDictionaries:")
    
    # Creating dictionaries
    person = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    empty = {}
    
    print(f"Person: {person}")
    print(f"Empty: {empty}")
    
    # Dictionary operations
    print("\nDictionary Operations:")
    person["email"] = "john@example.com"  # Add new key-value
    print(f"After adding email: {person}")
    
    age = person.get("age")  # Get value
    print(f"Age: {age}")
    
    # Default value if key doesn't exist
    country = person.get("country", "USA")
    print(f"Country: {country}")
    
    # Remove key
    del person["city"]
    print(f"After removing city: {person}")

def demonstrate_dictionary_methods():
    """Show dictionary methods"""
    print("\nDictionary Methods:")
    
    person = {"name": "John", "age": 30, "city": "New York"}
    
    # Keys, values, items
    print(f"Keys: {person.keys()}")
    print(f"Values: {person.values()}")
    print(f"Items: {person.items()}")
    
    # Update
    person.update({"age": 31, "email": "john@example.com"})
    print(f"After update: {person}")
    
    # Pop
    age = person.pop("age")
    print(f"Popped age: {age}")
    print(f"After pop: {person}")

def demonstrate_sets():
    """Show set examples"""
    print("\nSets:")
    
    # Creating sets
    fruits = {"apple", "banana", "cherry"}
    empty = set()  # Note: not {}
    
    print(f"Fruits: {fruits}")
    print(f"Empty: {empty}")
    
    # Set operations
    print("\nSet Operations:")
    fruits.add("orange")  # Add element
    print(f"After add: {fruits}")
    
    fruits.remove("banana")  # Remove element
    print(f"After remove: {fruits}")
    
    # Set operations
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference: {set1 - set2}")
    print(f"Symmetric difference: {set1 ^ set2}")

def demonstrate_set_methods():
    """Show set methods"""
    print("\nSet Methods:")
    
    numbers = {1, 2, 3, 4, 5}
    
    # Add multiple elements
    numbers.update({6, 7, 8})
    print(f"After update: {numbers}")
    
    # Remove element (no error if not present)
    numbers.discard(9)
    print(f"After discard: {numbers}")
    
    # Pop random element
    popped = numbers.pop()
    print(f"Popped: {popped}")
    print(f"After pop: {numbers}")

def main():
    print("Welcome to Python Dictionaries and Sets!")
    demonstrate_dictionaries()
    demonstrate_dictionary_methods()
    demonstrate_sets()
    demonstrate_set_methods()
    
    print("\nKey Points:")
    print("1. Dictionaries store key-value pairs")
    print("2. Sets store unique elements")
    print("3. Dictionary keys must be immutable")
    print("4. Sets are unordered and mutable")
    print("5. Both support various operations and methods")

if __name__ == "__main__":
    main() 