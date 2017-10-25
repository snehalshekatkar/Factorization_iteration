import natural_numbers as nn

a = 654
n = 89

for i in range(100):
    if nn.is_prime(n):
        n += a
        print(n)
    else:
        n = sum(nn.factorize(n))
        print(n)

    
