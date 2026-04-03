#include <iostream>
using namespace std;

double pwr(double base, int exp) {
    if (exp == 0)
        return 1;
    return base * pwr(base, exp - 1);
}

double series(int n, double r) {
    if (n < 0)
        return 0;
    return pwr(r, n) + series(n - 1, r);
}

int main() {
    int n;
    double r;
    cout << "Enter number of terms: ";
    cin >> n;
    cout << "Enter common ratio: ";
    cin >> r;
    double result = series(n, r);
    cout << "Gn = " << result << endl;
    return 0;
}