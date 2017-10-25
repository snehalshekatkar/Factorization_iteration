#include<iostream>
#include<math.h>
#include<vector>
using namespace std;

int is_prime(int n){

    if (n == 0 || n == 1){
        return false;
    }

    else if(n == 2){
        return true;
    }
    else{
    for (int i = 2; i < pow(n, 0.5) + 1; i++){
        if (n % i == 0){
            return false;
        }
    }

    return true;
    }

}

// Function that returns all the primes less than n
std::vector<int> primes_less_than(int n){
    std::vector<int> arr;
    for (int i = 2; i < n; i++){
       if (is_prime(i) == true){
            //cout << "beta " << i << endl;
            arr.push_back(i);
        }

    }

    //cout << arr << endl;
    for (int i = 0; i < arr.size(); i++){
        //cout << "alpha " << arr[i] << endl;
    }

    return arr;
}        
        
// This function returns all the prime factors of the number n
std::vector<int> factorize(int n){
    
    std::vector<int> factors;
    std:: vector<int> p = primes_less_than(n);
    for (int i = 0; i < p.size(); i++){
        if (n % p[i] == 0){
            int dummy_n = n;
            while (dummy_n % p[i] == 0 && dummy_n != 0){
                factors.push_back(p[i]);
                dummy_n /= p[i];
            }
        }
    }
    
    return factors;

}

int main()
{
    std:: vector<int> p = factorize(144);

    for (int i = 0; i < p.size(); i++){

        cout << p[i]  << endl;
    }
}
