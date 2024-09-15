import math

def is_prime(number):
    """
    Function to check if a number is prime.
    A number is prime if it is only divisible by 1 and itself.
    """
    if number <= 1:
        return False
    
    # Check divisibility from 2 up to sqrt(number)
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Example usage (commented out to prevent automatic execution)
# number = 29
# result = is_prime(number)
# print(f"{number} is {'prime' if result else 'not prime'}")
