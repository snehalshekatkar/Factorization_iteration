#include "natural_numbers.hh"

int main()
{
    std:: vector<int> p = factorize(20);

    int sum = 0;
    for (int i = 0; i < p.size(); i++){

        cout << p[i]  << endl;
        sum += p[i];
    }
    cout << "sum " << sum << endl;
}
