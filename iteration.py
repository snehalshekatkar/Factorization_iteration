import natural_numbers as nn

g = open('cycle_lengths.dat', 'w')

for b in range(1, 51):
    print(b)
    f = open('Output_data/output_b{}.dat'.format(b), 'w')
    
    all_l = []
    for i in range(1, 101):
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

    g.write(str(b) + '  ' + str(set(all_l)) + '\n')

g.close()
