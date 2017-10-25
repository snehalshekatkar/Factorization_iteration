import natural_numbers as nn

a = 1

f = open('Output_data/output_a{}.txt'.format(a), 'w')

for i in range(1, 10000):
    n = i
    seq = []

    ''' Iterate starting with n till the cycle is reached '''
    T = -1
    while n not in seq:
        T += 1
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

    print(i, T, cycle)        
    f.write(str(i) + ',' + str(len(cycle)) + ',' + str(T) + ',' + str(cycle) + '\n')
    
