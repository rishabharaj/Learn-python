def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

help(add)

# Help on function add:

# add(a, b)
#     Returns the sum of two numbers.

class Student:
    """Represents a student."""

    def __init__(self, name):
        self.name = name

help(Student)
Help on class Student:

# class Student
#  |  Represents a student.
#  |
#  |  Methods defined here:
#  |      __init__(self, name)


#Comments (using #) explain how the code works internally 
#and are completely ignored by Python at runtime.
#Docstrings (using """) explain what a function or class does 
#and stay alive at runtime so users can read them using the help() function
