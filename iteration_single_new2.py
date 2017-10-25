import natural_numbers as nn

a = 1

for i in range(1, 10):
    n = i
    seq = []

    ''' Iterate starting with n till the cycle is reached '''
    while n not in seq:
        seq.append(n)
        if nn.is_prime(n):
            n += a
        else:
            n = sum(nn.factorize(n))

    ''' Extract the cycle '''
    seq.append(n) # This is important so that n will appear twice in the sequence
    if len(seq) > 1:
        j = -2
        x = seq[-1]
        cycle = [x]
        while x != seq[j]:
            cycle.append(seq[j])
            j -= 1
    else:
        cycle = seq

        
    
