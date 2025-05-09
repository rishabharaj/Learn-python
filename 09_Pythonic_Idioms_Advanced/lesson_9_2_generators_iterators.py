"""
Lesson 9.2: Generators and Iterators

This lesson covers:
- Generator functions
- Iterator protocol
- yield keyword
- Lazy evaluation
- Memory efficiency
"""

from typing import Iterator, Generator, List
import sys

class FibonacciIterator:
    """Iterator that generates Fibonacci numbers"""
    
    def __init__(self, limit: int):
        self.limit = limit
        self.a, self.b = 0, 1
        self.count = 0
    
    def __iter__(self) -> 'FibonacciIterator':
        return self
    
    def __next__(self) -> int:
        if self.count >= self.limit:
            raise StopIteration
        
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """Generator function that yields Fibonacci numbers"""
    a, b = 0, 1
    count = 0
    
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

def memory_comparison() -> None:
    """Compare memory usage between list and generator"""
    # Using list
    print("Memory usage with list:")
    numbers = [x for x in range(1000000)]
    print(f"Size of list: {sys.getsizeof(numbers)} bytes")
    
    # Using generator
    print("\nMemory usage with generator:")
    numbers_gen = (x for x in range(1000000))
    print(f"Size of generator: {sys.getsizeof(numbers_gen)} bytes")

def custom_range(start: int, stop: int, step: int = 1) -> Generator[int, None, None]:
    """Custom range generator"""
    current = start
    while current < stop:
        yield current
        current += step

def main() -> None:
    """Main function to demonstrate generators and iterators"""
    # Using the iterator
    print("Fibonacci numbers using iterator:")
    fib_iter = FibonacciIterator(10)
    for num in fib_iter:
        print(num, end=" ")
    print()
    
    # Using the generator
    print("\nFibonacci numbers using generator:")
    for num in fibonacci_generator(10):
        print(num, end=" ")
    print()
    
    # Memory comparison
    print("\n=== Memory Usage Comparison ===")
    memory_comparison()
    
    # Custom range generator
    print("\n=== Custom Range Generator ===")
    print("Even numbers from 0 to 10:")
    for num in custom_range(0, 10, 2):
        print(num, end=" ")
    print()

if __name__ == "__main__":
    main() 