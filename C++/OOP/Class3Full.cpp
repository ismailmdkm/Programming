// Simple class created in stack
#include <iostream>
using namespace std;

class Rectangle {
private:
  int length;
  int breadth;

public:
  // default construcor (Inline since defined inside the class)
  Rectangle() {
    length = 1;
    this->breadth = 1;
  };
  // Parameterized constructore definition
  Rectangle(int, int);
  // copy constructor definition
  Rectangle(Rectangle &r);
  // Getter or Accessor for length
  int getLength() { return length; }
  // Getter or Accessor for breadth
  int getBreadth() { return breadth; }
  // Setter or Mutator for length
  void setLength(int l) {
    if (l >= 0)
      length = l;
    else
      length = 0;
  }
  // Setter or Mutator for breadth
  void setBreadth(int breadth) {
    if (breadth >= 0)
      this->breadth = breadth;
    else
      this->breadth = 0;
  }
  // Get area of rectangle
  int area() { return length * breadth; }
  int perimeter();
  bool isSquare() { return length == breadth; }
};
// Parameterized constructor - (Not inline since defined outside the class)
Rectangle::Rectangle(int l, int breadth) {
  length = l;
  this->breadth = breadth; //'this' pointer is used to retrieve object's
                           //'breadth' hidden by local variable 'breadth'
}
// Copy constructor - (Inline since defined with keyword 'inline')
inline Rectangle::Rectangle(Rectangle &r) {
  length = r.length;
  breadth = r.breadth;
}
// Get perimeter of rectangle
int Rectangle::perimeter() {
  int var1 = 0;
  cout << "before div by 0" << endl;
  return 2 * (length + breadth) / var12;
  cout << "after div by 0" << endl;
}
// main section starts here
int main() {
  Rectangle r1; // default constructor will be called. It is invalid to give
                // empty braces()
  cout << r1.area() << endl;
  Rectangle r2(10, 15); // Parameterized constructor is called
  cout << r2.area() << endl;
  Rectangle r3(r2); // Also we can do "Rectangle r3=r2"
  cout << r3.perimeter() << endl;
  Rectangle r4;
  r4 = r3;
  cout << r3.perimeter() << endl;
  return 0;
}