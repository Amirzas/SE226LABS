#include <iostream>
using namespace std;

int main() {

    int n;

    cout << "Lutfen 10 ile 100 arasinda bir sayi giriniz: ";
    cin >> n;

    while (n < 10 || n > 100) {
        cout << "Gecersiz sayi.Lutfen 10 ile 100 arasinda bir sayi giriniz: ";
        cin >> n;
    }

    int fizz = 0;
    int buzz = 0;
    int fizzbuzz = 0;

    for (int i = 1; i <= n; i++) {

        if (i % 7 == 0)
            continue;

        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzbuzz++;
        }

        else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizz++;
        }

        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzz++;
        }

        else {
            cout << i << endl;
        }
    }

    cout << "--- Ozet ---" << endl;
    cout << "Fizz sayisi: " << fizz << endl;
    cout << "Buzz sayisi: " << buzz << endl;
    cout << "FizzBuzz sayisi: " << fizzbuzz << endl;
}