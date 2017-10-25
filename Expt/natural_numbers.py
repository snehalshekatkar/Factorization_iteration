import math

''' The function is_prime checks whether the given number n is prime'''
def is_prime(n):
    if n == 1:
        return False

    if type(n) == float:
        print("Integer input required")
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
       if n % i == 0:
            return False 
    return True

''' The following function returns the number of primes less than n excluding n itself'''
def primes_less_than(n):
    if type(n) == float:
        print("Integer input required")
        return None

    if n < 2:
        return None

    primes = []
    for i in range(2, n):
       if is_prime(i):
            primes.append(i)
    return primes

''' The following function factorizes a given natural number into the product of primes'''
def factorize(n):
    if type(n) == float:
        print("Input type must be int")
        return None

    if n < 1:
        print("Input must be a natural number")
        return None

    if n == 1 or is_prime(n):
        return [n]

    factors = []
    for prime in primes_less_than(n) :
        if n % prime == 0:
            tot = 0
            dummy_n = n 
            while dummy_n % prime == 0 and dummy_n != 0 :
                factors.append(prime)
                dummy_n = dummy_n // prime
   # start_number = 2
   # while not is_prime(n):
   #     print("alpha", n)
   #     if start_number < int(math.sqrt(n)) + 1 :
   #         for i in range(start_number, int(math.sqrt(n)) + 1):
   #             if n % i == 0 :
   #                 print(i)
   #                 factors.append(i)
   #                 n = n // i
   #                 break
                            
    return factors
 
