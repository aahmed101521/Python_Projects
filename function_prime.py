# Define function for prime number 

import math

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


number = input("provide the number:")
value = is_prime(int(number))
print(f'the number {number} is prime:  {value}')