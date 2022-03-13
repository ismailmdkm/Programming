#include <iostream>
using namespace std;
// debug and understand the scope of 'x'
int x = 10;
int main() { 
    cout << x << endl; // in debug, it is not showing '10' but printing
    int x = 20;
    cout << x << endl;
    {
        cout << x << endl; // again, in debug, not showing correct value, but printing '20'
        int x = 30;
        cout << x << endl;
    }
    cout << x << endl;
    cout << ::x << endl; // Access global variable using scope resolution operator
    return 0;
}