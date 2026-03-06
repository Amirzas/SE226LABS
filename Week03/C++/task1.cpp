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