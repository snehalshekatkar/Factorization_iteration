import natural_numbers as nn

g = open('cycles.txt', 'w')
g1 = open('signs.txt', 'w')

for a in range(1, 501):
    
    print(a)
    all_cycles = []
    cycles_signs = {}
    all_l = [] # This array stores the lengths of cycles for each n
    f = open('Output_data/output_a{}.txt'.format(a), 'w')
    
    for i in range(1, 201):
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
    
        cycle.reverse()
        all_cycles.append(cycle)
        all_l.append(len(cycle))

        

        '''Assign the signs to members of the cycle'''
        signs = [1 if nn.is_prime(x) else 0 for x in cycle]

        if str(cycle) not in {str([4]), str([1])}:
            cycles_signs[str(cycle)] = signs

        f.write(str(i) + ',' + str(len(cycle)) + ',' + str(T) + ',' + str(cycle) + '\n')
        
    f.close()


    ''' Find the frequencies of unique cycles '''    
    all_cycles = list(map(tuple, all_cycles))
    freq = {x:all_cycles.count(x) for x in all_cycles}

    ''' Write the output in files'''
    g.write(str(a) + '  ' + str(len(freq)) + '  ' +  str(freq) + '\n')
    g.write('\n')
    g1.write(str(a) + '  ' + str(cycles_signs) + '\n')
    g1.write('\n')


f.close()
g.close()
g1.close()


