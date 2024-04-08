# Write your code below this line 👇
import math

def prime_checker(number):
    if number <= 1:
        print("It's not a prime number.")
        return
    elif number == 2:
        print("It's a prime number.")
        return

    max_divisor = math.isqrt(number)  # Use square root for efficiency
    for n in range(2, max_divisor + 1):
        if number % n == 0:
            print("It's not a prime number.")
            return

    print("It's a prime number.")

print("Welcome to the prime number checker. Enter a number to check if it's prime.")
n = int(input()) # Check this number
prime_checker(number=n)