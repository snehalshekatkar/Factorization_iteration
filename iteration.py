import natural_numbers as nn

''' Open the file to save the lengths of cycles for each b '''
g = open('cycle_lengths.dat', 'a')


''' Loop over b '''
for b in range(1, 201):
    print(b)
    f = open('Output_data/output_b{}.dat'.format(b), 'w')
    
    all_l = [] # This array stores the lengths of cycles for each n > 4
    for i in range(1, 105):
        l = 0
        stop = False
        n = i    
        asympt = []
        for t in range(50):
            if nn.is_prime(n):
                n += b
                if t > 30:
                    asympt.append(n)
                    if t == 31:
                        N = n
                        l += 1
                    elif t > 31 and N != n and not stop:
                        l += 1
                    else:
                        stop = True
                    
            else:
                n = sum(nn.factorize(n))
                if t > 30:
                    asympt.append(n)
                    if t == 31:
                        N = n
                        l += 1
                    elif t > 31 and N != n and not stop:
                        l += 1
                    else:
                        stop = True

        f.write(str(i) + '  ' + str(l) + '  ' + str(asympt) + '\n')
        if i > 4:
            all_l.append(l)
            
    f.close()        

    freq = {x:all_l.count(x) for x in all_l}
    g.write(str(b) + '  ' + ' ' + str(len(freq)) + '  ' +  str(freq) + '\n')

g.close()
