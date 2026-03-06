#include <iostream>
using namespace std;

int main() {

    int x;
    cout << "9'dan büyük bir sayi giriniz: ";
    cin >> x;

    int step = 0;

    cout << x;

    while (x > 9) {

        int temp = x;
        int toplam = 0;

        while (temp > 0) {
            int kalan = temp % 10;
            toplam += kalan;
            temp /= 10;
        }

        x = toplam;
        step++;

        cout << " -> " << x;
    }

    cout << endl;
    cout << "Final deger: " << x << endl;
    cout << "Toplam adim: " << step << endl;

}
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
#include <iostream>
using namespace std;

int main() {

    int n;

    cout << "Lutfen 3 ile 9 arasinda bir sayi girin: ";
    cin >> n;

    while (n < 3 || n > 9) {
        cout << "Gecersiz sayi.Lutfen 3 ile 9 arasinda bir sayi girin: ";
        cin >> n;
    }

    for (int i = 1; i <= n; i++) {

        for (int j = 1; j <= i; j++) {
            cout << j;
        }

        cout << endl;
    }

    for (int i = n - 1; i >= 1; i--) {

        for (int j = 1; j <= i; j++) {
            cout << j;
        }

        cout << endl;
    }
}