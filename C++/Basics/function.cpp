// Added comment to test git
#include <iostream>
using namespace std;

int max(int, int);

int main()
{
    int a, b;
    cout << "Enter 1st number: ";
    cin >> a;
    cout << "Enter 2nd number: ";
    cin >> b;
    cout << "Max is: " << max(a, b) << endl;
};
int max(int num1, int num2)
{
    if (num1 > num2)
        return num1;
    else
        return num2;
};