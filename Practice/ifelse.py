num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
if num1 > num2:
    print("First number is greater than second number")
else:
    print("First number is less than second number")
# This will not work in cmd mode, as input() returns a string
#print("sum of this two numbers is: ", num1 + num2)
print("sum of this two numbers is: ", int(num1) + int(num2))
