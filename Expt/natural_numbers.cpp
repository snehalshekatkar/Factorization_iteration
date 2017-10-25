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

int primes_less_than(int n){
    vector<int> arr;
    for (int i = 2; i < n; i++){
       if (is_prime(i) == true){
            cout << "beta " << i << endl;
            arr.push_back(i);
        }

    }

    //cout << arr << endl;
    for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++){
        cout << "alpha " << arr[i] << endl;
    }
    return 0;
}        
        

int *factorize(int n){
    
    if (n == 0 || n == 1){
        return 0;
    }

}

int main()
{
    for (int i = 0; i < 20; i++){
        cout << i << "," << is_prime(i) << endl;
    }
    //primes_less_than(20);
}
