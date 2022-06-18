// Simple class created in stack
#include <iostream>
using namespace std;

class Rectangle {
public:
  int length;
  int breadth;
  int area() { return length * breadth; }
  int perimeter() { return 2 * (length + breadth); }
};

int main() {
  // Object in Stack
  Rectangle r1;  // object r1 will be created in stack
  Rectangle *p1; // Also can be in one line *p = &r1 to assign pointer to object
  p1 = &r1;
  r1.length = 10;
  p1->breadth = 5;
  cout << r1.area() << endl;       // Access function using . operator
  cout << p1->perimeter() << endl; // Also can access function using pointer
                                   // with dereference or arrow operator
  // Object in heap
  Rectangle *p2 = new Rectangle();
  p2->length = 10;
  p2->breadth = 5;
  cout << p2->area() << endl;
  cout << p2->perimeter() << endl;
  return 0;
}