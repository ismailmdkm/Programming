#include <iostream>
#include <vector>
using namespace std;
// declare function with auto return type
auto add(auto x, int y) {
  int sum = x + y;
  return sum;
}
// define template using auto
template <typename T> auto product(T x, T y) {
  // calculate product
  return x * y;
}
int main() {
  // use auto keyword to declare a variable
  auto weight = 55.6;
  auto age = 32;
  cout << "Weight is " << weight << " kg and age is " << age << endl;
  // double
  auto d = 7.9;
  // float using suffix f
  auto f = 6.7f;
  // unsigned long using suffix ul
  auto u = 66ul;
  // string using suffix s
  auto st = "store"s;
  // can also use with constant
  const auto var = st;
  // Auto deduce type to be index in array
  int arr1[] = {4, 5, 6};
  for (auto idx = 0; idx < size(arr1); idx++) {
    cout << arr1[idx] << " ";
  }
  cout << "\n";
  // Using auto in for-each loop
  for (auto value : arr1) {
    cout << value << " ";
  }
  cout << "\n";
  // Auto deduce type to be iterator of a vector of ints.
  vector<int> vec1{1, 2, 3};
  for (auto it = vec1.begin(); it != vec1.end(); it++) {
    cout << *it << " ";
  }
  cout << "\n";
  cout << add(5, 6) << endl;
  cout << product(5, 6) << endl;
  // Auto in pointers
  int num1 = 10, num2 = 9;
  // declare pointer using auto
  auto p1 = &num1;
  // we can also use * for readability
  auto* p2 = &num2;
  cout << "The values are " << *p1 << " and " << *p2 << endl;
  // declare reference using auto
  auto& x = num1;
  // change the value of num1 to see if the reference works
  num1 = 19;
  cout << "The value is " << x << endl;
  return 0;
}