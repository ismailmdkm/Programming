#include <iostream>
using namespace std;

int main()
{
    // defining enum for Gender (new data type)
    enum Gender
    {
        Male,
        Female
    };

    // Creation Gender variable and initializing with value
    Gender gender = Male;

    if (gender == Male)
        cout << "Gender is Male";
    else if (gender == Female)
        cout << "Gender is Female";
    else
        cout << "Invalid entry";
    return 0;
};