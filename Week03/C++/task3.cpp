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