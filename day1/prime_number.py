# Function to check if a number is prime
def is_prime(number):
    if number <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(number ** 0.5) + 1):  # Check divisibility up to the square root of the number
        if number % i == 0:  # If divisible by any number other than 1 and itself, it's not prime
            return False
    return True  # If no divisors are found, the number is prime

# Input from user
num = 17

# Check if the number is prime
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

