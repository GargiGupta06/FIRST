import math

# Function to check perfect square
def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

# Function to check if n is a Fibonacci number
def is_fibonacci(n):
    # A number is Fibonacci if and only if one of the following is a perfect square:
    # (5*n^2 + 4) or (5*n^2 - 4)
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Input from user
num = int(input("Enter a number: "))

# Check and print result
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is NOT a Fibonacci number.")
