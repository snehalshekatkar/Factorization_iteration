import pandas as pd
import matplotlib.pyplot as plt

for N, color in zip([500000, 1000000], ['b', 'r']):
    df = pd.read_csv('sum_is_prime_N{}.txt'.format(N), names = ["n", "sum"])
    df.groupby("sum").count().to_csv('similar_numbers_count.txt')
    
    #dg = df.groupby("sum").count()
    dg = pd.read_csv('similar_numbers_count.txt')
    
    plt.plot(dg["sum"], dg["n"], '.', color = color, label = "N = {}".format(N))
    plt.legend()
    
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r"$p$")
plt.ylabel(r"Total numbers which fall to p")
plt.savefig('similar_number_count.pdf')

