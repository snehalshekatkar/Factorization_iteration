import natural_numbers as nn

''' Open the file to save the lengths of cycles for each b '''
g = open('cycles.txt', 'a')
g1 = open('sings.txt', 'a')

''' Loop over b '''
for b in range(201, 1001):
    print(b)
    cycles = {}
    f = open('Output_data/output_b{}.txt'.format(b), 'w')
    
    all_l = [] # This array stores the lengths of cycles for each n > 4
    for i in range(1, 101):
        l = 0
        stop = False
        n = i    
        all_vals = [n]
        asympt = []
        for t in range(100):
            if nn.is_prime(n):
                n += b
                all_vals.append(n)
                if t > 30:
                    if t == 31:
                        N = n
                        l += 1
                        asympt.append(n)
                    elif t > 31 and N != n and not stop:
                        l += 1
                        asympt.append(n)
                    else:
                        stop = True
                    
            else:
                n = sum(nn.factorize(n))
                all_vals.append(n)
                if t > 30:
                    if t == 31:
                        N = n
                        l += 1
                        asympt.append(n)
                    elif t > 31 and N != n and not stop:
                        l += 1
                        asympt.append(n)
                    else:
                        stop = True

        ''' Find the time to reach the cycle'''
        T = 0
        for x in all_vals:
            if x not in asympt:
                T += 1
            else:
                break

        cycle = all_vals[T : T + len(asympt)]
        cycle.sort()

        '''Assign the signs to members of the cycle'''
        signs = [1 if nn.is_prime(x) else 0 for x in cycle]

        if str(cycle) not in {str([4]), str([1])}:
            cycles[str(cycle)] = signs
        
        f.write(str(i) + ',' + str(l) + ',' + str(T) + ',' + str(cycle) + ',' + str(signs) + '\n')
        #f.write(str(i) + '  ' + str(l) + '  ' + str(T) + ' ' + str(all_vals) + '\n')
        if i > 4:
            all_l.append(l)
            
    f.close()        

    freq = {x:all_l.count(x) for x in all_l}
    g.write(str(b) + ',' + str(len(freq)) + ',' +  str(freq) + '\n')
    g1.write(str(b) + ',' + str(cycles) + '\n')
    g1.write('\n')

g.close()
g1.close()
