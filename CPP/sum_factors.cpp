#include "natural_numbers.hh"
#include<fstream>

int main(){

    // Open a file to store the value of the sum of the divisors
    ofstream f1;
    ofstream f2;
    ofstream f3;
    f1.open("sum_prime_factors.txt");
    f2.open("ratio.txt");
    f3.open("sum_is_prime_N500000.txt");
    
    int N = 500000;
    int sum[N] = {0};
    int dummy[N];
    for (int i = 0; i < N; i++){
        dummy[i] = i+1;
    }
    sum[0] = 1;


    std::vector <int> primes = primes_less_than(N+1);
    int tot_numbers[primes.size()] = {0};
    
    // Loop over primes less than N
    for (int i = 0; i < primes.size(); i++){

        int p = primes[i];

        // Add the prime p to all its multiples
        for (int j = 1; j <= N/p; j++){
            while (dummy[j*p-1] % p == 0){
                sum[j*p-1] += p;
                dummy[j*p-1] /= p;
            }
        }
    }
    
    // Write to the output files
    for (int i = 0; i < N; i++){
        f1 << i+1 << "," << sum[i] << endl;
        f2 << i+1 << "," << float(sum[i])/(i+1) << endl;
        if (is_prime(sum[i])){
            f3 << i+1 << "," << sum[i] << endl;
        }
    }

    f1.close();
    f2.close();
    f3.close();
}

