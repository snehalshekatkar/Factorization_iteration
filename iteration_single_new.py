import natural_numbers as nn

a = 654 

for i in range(89, 100):
    n = i
    seq = [n]
    seq2 = [n]
    first_term = True

    ''' Iterate starting with n'''
    while n not in seq2 or first_term:
        first_term = False
        if nn.is_prime(n):
            n += a
        else:
            n = sum(nn.factorize(n))
        seq2.append(n)
        seq.append(n)

    ''' Extract the cycle '''
    if len(seq2) > 2:
        j = -2
        x = seq2[-1]
        cycle = [x]
        while x != seq2[j]:
            cycle.append(seq2[j])
            j -= 1
    else:
        cycle = seq2

    print(i, seq, seq2)
    print()
        
    
