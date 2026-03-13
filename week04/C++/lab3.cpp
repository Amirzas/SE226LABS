#include <iostream>
using namespace std;

    void swapValues(int* p1,int*p2){
        int temp=*p1;
        *p1=*p2;
        *p2=temp;
    }
void printArray(int* arr, int size) {
    for(int i = 0; i < size; i++) {
        cout << *(arr + i) << " ";
    }
}
int findMax(int* arr, int size) {
    int temp=arr[0];
    for(int i = 1; i < size; i++) {
        if(*(arr + i) > temp) {
            temp = *(arr + i);
        }
    }
}
void reverseArray(int* arr, int size) {
    for(int i = 0; i < size/2; i++) {
        int temp = *(arr + i);
        *(arr + i) = *(arr + size - 1 - i);
        *(arr + size - 1 - i) = temp;
    }
}
int* createArray(int size) {
    int* arr = new int[size];
    return arr;
}
void deleteArray(int* arr) {
    delete[] arr;
}
int main() {

    }