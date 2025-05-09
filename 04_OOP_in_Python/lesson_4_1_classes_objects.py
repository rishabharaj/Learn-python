"""
Lesson 4.1: Classes and Objects

This lesson covers:
1. Class definition
2. Object instantiation
3. Instance variables
4. Methods
5. Special methods

Key differences from Java:
- No access modifiers (public, private, protected)
- No method overloading
- self parameter in methods
- Special methods (__init__, __str__, etc.)
- Properties and descriptors
"""

class Person:
    """A simple class representing a person"""
    
    def __init__(self, name: str, age: int):
        """Initialize a new Person
        
        Args:
            name: The person's name
            age: The person's age
        """
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        """Return a greeting message
        
        Returns:
            A greeting string
        """
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def __str__(self) -> str:
        """Return a string representation of the person
        
        Returns:
            A string representation
        """
        return f"Person(name='{self.name}', age={self.age})"

class BankAccount:
    """A class representing a bank account"""
    
    def __init__(self, account_number: str, balance: float = 0.0):
        """Initialize a new bank account
        
        Args:
            account_number: The account number
            balance: Initial balance (default 0.0)
        """
        self.account_number = account_number
        self._balance = balance  # Convention: _ means "protected"
    
    def deposit(self, amount: float) -> None:
        """Deposit money into the account
        
        Args:
            amount: The amount to deposit
        """
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account
        
        Args:
            amount: The amount to withdraw
            
        Returns:
            True if successful, False otherwise
        """
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount:.2f}")
            return True
        print("Withdrawal failed")
        return False
    
    def get_balance(self) -> float:
        """Get the current balance
        
        Returns:
            The current balance
        """
        return self._balance

class Rectangle:
    """A class representing a rectangle"""
    
    def __init__(self, width: float, height: float):
        """Initialize a new rectangle
        
        Args:
            width: The rectangle's width
            height: The rectangle's height
        """
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """Calculate the area
        
        Returns:
            The area of the rectangle
        """
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Calculate the perimeter
        
        Returns:
            The perimeter of the rectangle
        """
        return 2 * (self.width + self.height)
    
    def __eq__(self, other) -> bool:
        """Check if two rectangles are equal
        
        Args:
            other: Another rectangle to compare with
            
        Returns:
            True if equal, False otherwise
        """
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.height == other.height

def demonstrate_classes():
    """Show class and object examples"""
    print("\nClass and Object Examples:")
    
    # Create a Person
    person = Person("Alice", 25)
    print(person.greet())
    print(person)  # Uses __str__
    
    # Create a BankAccount
    account = BankAccount("123456", 100.0)
    account.deposit(50.0)
    account.withdraw(25.0)
    print(f"Balance: ${account.get_balance():.2f}")
    
    # Create Rectangles
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(4, 5)
    rect3 = Rectangle(3, 6)
    
    print(f"Rectangle 1 area: {rect1.area()}")
    print(f"Rectangle 1 perimeter: {rect1.perimeter()}")
    print(f"Rectangle 1 == Rectangle 2: {rect1 == rect2}")
    print(f"Rectangle 1 == Rectangle 3: {rect1 == rect3}")

def demonstrate_properties():
    """Show property examples"""
    print("\nProperty Examples:")
    
    class Temperature:
        def __init__(self, celsius: float):
            self._celsius = celsius
        
        @property
        def celsius(self) -> float:
            return self._celsius
        
        @celsius.setter
        def celsius(self, value: float) -> None:
            self._celsius = value
        
        @property
        def fahrenheit(self) -> float:
            return (self._celsius * 9/5) + 32
        
        @fahrenheit.setter
        def fahrenheit(self, value: float) -> None:
            self._celsius = (value - 32) * 5/9
    
    temp = Temperature(25)
    print(f"Celsius: {temp.celsius}°C")
    print(f"Fahrenheit: {temp.fahrenheit}°F")
    
    temp.fahrenheit = 98.6
    print(f"After setting Fahrenheit: {temp.celsius}°C")

def main():
    print("Welcome to Python Classes and Objects!")
    demonstrate_classes()
    demonstrate_properties()
    
    print("\nKey Points:")
    print("1. Classes are defined with class keyword")
    print("2. __init__ is the constructor")
    print("3. Methods take self as first parameter")
    print("4. Properties can be used for computed attributes")
    print("5. Special methods start and end with __")

if __name__ == "__main__":
    main() 