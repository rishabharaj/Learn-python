"""
Lesson 10.1: Introduction to unittest

This lesson covers:
- unittest framework
- Test cases and suites
- Assertions
- Test discovery
- Test fixtures
"""

import unittest
from typing import List

# Example functions to test
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def filter_even(numbers: List[int]) -> List[int]:
    """Filter even numbers from a list"""
    return [x for x in numbers if x % 2 == 0]

# Test cases
class TestMathOperations(unittest.TestCase):
    """Test cases for math operations"""
    
    def setUp(self) -> None:
        """Set up test fixtures"""
        self.test_numbers = [1, 2, 3, 4, 5]
    
    def test_add(self) -> None:
        """Test addition function"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_divide(self) -> None:
        """Test division function"""
        self.assertEqual(divide(6, 2), 3.0)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertRaises(ValueError, divide, 5, 0)
    
    def test_filter_even(self) -> None:
        """Test even number filtering"""
        result = filter_even(self.test_numbers)
        self.assertEqual(result, [2, 4])
        self.assertNotIn(1, result)
        self.assertNotIn(3, result)
        self.assertNotIn(5, result)

# Test suite
def create_test_suite() -> unittest.TestSuite:
    """Create a test suite"""
    suite = unittest.TestSuite()
    suite.addTest(TestMathOperations('test_add'))
    suite.addTest(TestMathOperations('test_divide'))
    suite.addTest(TestMathOperations('test_filter_even'))
    return suite

def main() -> None:
    """Main function to run tests"""
    # Run individual test case
    print("Running individual test case:")
    unittest.main(argv=[''], exit=False)
    
    # Run test suite
    print("\nRunning test suite:")
    runner = unittest.TextTestRunner()
    suite = create_test_suite()
    runner.run(suite)

if __name__ == "__main__":
    main() 