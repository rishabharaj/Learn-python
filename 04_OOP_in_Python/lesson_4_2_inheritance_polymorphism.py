"""
Lesson 4.2: Inheritance and Polymorphism

This lesson covers:
1. Single inheritance
2. Method overriding
3. super() function
4. Abstract base classes
5. Duck typing

Key differences from Java:
- Multiple inheritance is allowed
- No interfaces (use abstract base classes)
- Duck typing instead of interface implementation
- super() is more flexible
- No abstract keyword
"""

from abc import ABC, abstractmethod
from typing import List

class Animal(ABC):
    """Abstract base class for animals"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def make_sound(self) -> str:
        """Make the animal's sound
        
        Returns:
            The sound the animal makes
        """
        pass
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"

class Dog(Animal):
    """A class representing a dog"""
    
    def make_sound(self) -> str:
        return "Woof!"
    
    def fetch(self) -> str:
        return f"{self.name} fetches the ball"

class Cat(Animal):
    """A class representing a cat"""
    
    def make_sound(self) -> str:
        return "Meow!"
    
    def climb(self) -> str:
        return f"{self.name} climbs the tree"

class Shape:
    """Base class for shapes"""
    
    def area(self) -> float:
        """Calculate the area
        
        Returns:
            The area of the shape
        """
        raise NotImplementedError("Subclasses must implement area()")
    
    def perimeter(self) -> float:
        """Calculate the perimeter
        
        Returns:
            The perimeter of the shape
        """
        raise NotImplementedError("Subclasses must implement perimeter()")

class Rectangle(Shape):
    """A class representing a rectangle"""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Circle(Shape):
    """A class representing a circle"""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius

class Employee:
    """Base class for employees"""
    
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
    
    def get_salary(self) -> float:
        return self.salary

class Manager(Employee):
    """A class representing a manager"""
    
    def __init__(self, name: str, salary: float, bonus: float):
        super().__init__(name, salary)
        self.bonus = bonus
    
    def get_salary(self) -> float:
        return super().get_salary() + self.bonus

def demonstrate_inheritance():
    """Show inheritance examples"""
    print("\nInheritance Examples:")
    
    # Create animals
    dog = Dog("Rex")
    cat = Cat("Whiskers")
    
    print(dog)
    print(f"{dog.name} says: {dog.make_sound()}")
    print(dog.fetch())
    
    print(cat)
    print(f"{cat.name} says: {cat.make_sound()}")
    print(cat.climb())

def demonstrate_polymorphism():
    """Show polymorphism examples"""
    print("\nPolymorphism Examples:")
    
    # Create shapes
    shapes: List[Shape] = [
        Rectangle(4, 5),
        Circle(3)
    ]
    
    for shape in shapes:
        print(f"{shape.__class__.__name__}:")
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")

def demonstrate_super():
    """Show super() function examples"""
    print("\nSuper() Examples:")
    
    # Create employees
    employee = Employee("John", 50000)
    manager = Manager("Alice", 60000, 10000)
    
    print(f"{employee.name}'s salary: ${employee.get_salary():.2f}")
    print(f"{manager.name}'s salary: ${manager.get_salary():.2f}")

def demonstrate_duck_typing():
    """Show duck typing examples"""
    print("\nDuck Typing Examples:")
    
    class Duck:
        def quack(self):
            return "Quack!"
    
    class Person:
        def quack(self):
            return "I'm pretending to be a duck!"
    
    def make_it_quack(duck_like):
        print(duck_like.quack())
    
    # Both objects can be used interchangeably
    make_it_quack(Duck())
    make_it_quack(Person())

def main():
    print("Welcome to Python Inheritance and Polymorphism!")
    demonstrate_inheritance()
    demonstrate_polymorphism()
    demonstrate_super()
    demonstrate_duck_typing()
    
    print("\nKey Points:")
    print("1. Python supports single and multiple inheritance")
    print("2. super() calls the parent class's methods")
    print("3. Abstract base classes can define interfaces")
    print("4. Duck typing allows flexible polymorphism")
    print("5. Method overriding is done by redefining methods")

if __name__ == "__main__":
    main() 