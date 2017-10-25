import natural_numbers as nn

f = open('Bn.txt', 'a')

a = 1
for i in range(1, 2001):
    print(i)
    if nn.is_prime(i):
        x = i + a
    else:
        x = sum(nn.factorize(i))

    f.write(str(i) + ',' + str(x) + '\n')

f.close()
