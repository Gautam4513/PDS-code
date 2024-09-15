# Que-6	Write a python program to find the factorial of a given number using recursion. OR Write a python code to find factorial of number using function. OR Write a python program that finds the factorial of a natural number n
# Function to calculate factorial using recursion
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Input: User provides the number
num = int(input("Enter a number: "))

# Checking if the number is a natural number (non-negative)
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calling the recursive function and printing the result
    print(f"The factorial of {num} is: {factorial(num)}")
