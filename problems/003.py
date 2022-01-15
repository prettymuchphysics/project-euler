# problem number: 003

import numpy as np

# N = 13195
N = 600851475143

def get_largest_prime_factor(num):
    for i in range(2, num//2+1):
        while num%i==0: num = num / i
        if num == 1: break
    return i

print(f'The answer is: {get_largest_prime_factor(N)}.')