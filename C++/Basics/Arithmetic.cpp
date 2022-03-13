#include <iostream>
using namespace std;

int main()
{
    int a = 10, b = 5, c;
    c = a + b;
    cout << "Result of " << a << " + " << b << ": " << c << endl;
    c = a - b;
    cout << "Result of " << a << " - " << b << ": " << c << endl;
    c = b - a;
    cout << "Result of " << b << " - " << a << ": " << c << endl;
    c = a * b;
    cout << "Result of " << a << " * " << b << ": " << c << endl;
    c = a / b;
    cout << "Result of " << a << " / " << b << ": " << c << endl;
    c = a % b;
    cout << "Result of " << a << " % " << b << ": " << c << endl;
    a = 17;
    b = 5;
    c = a / b;
    cout << "Result of " << a << " / " << b << ": " << c << endl;
    c = a % b;
    cout << "Result of " << a << " % " << b << ": " << c << endl;
    float d;
    d = a / b;
    cout << "Result of " << a << " / " << b << ": " << d << endl;
    d = (float)a / b;
    cout << "With typecast " << a << " / " << b << ": " << d << endl;
    float e = 17, f = 5;
    d = e / f;
    cout << "Result of " << e << " / " << f << ": " << d << endl;
    // d = e % f; Mod operation possible only on integer and characters
    // cout << "Result of " << e << " % " << f << ": " << d << endl;
    char g = 65; // ASCII code of A
    cout << "Character " << g << endl;
    g = 'A';
    cout << "Character " << g << endl;
    g = g + 1;
    cout << "Character " << g << endl;
    return 0;
};