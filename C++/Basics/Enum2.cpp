#include <iostream>
using namespace std;
// defining enum for Year (new data type)
enum Year
{
    Jan,
    Feb,
    Mar,
    Apr = 6,
    May,
    Jun,
    Jul,
    Aug,
    Sup = 20,
    Oct,
    Nov,
    Dec
};

int main()
{
    // Example to get the code value (i.e. numeric value assigned for each element)
    int i;
    for (i = Jan; i <= Dec; i++)
    {
        cout << i << " ";
    }
    return 0;
};