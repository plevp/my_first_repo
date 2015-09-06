#include <iostream>
using namespace std;


class Base {
private:
protected:
  int a_i;

public:
  Base(int i_) { 
    a_i = i_;
  };
  virtual void print() {
    cout<< "Class B " << a_i << endl;
  }
};

class ABase {
private:
protected:
  int a_i;

public:
  ABase(int i_) { 
    a_i = i_;
  };
  virtual void print() {
    cout<< "Class AB " << a_i << endl;
  }
};

class DerivedA : public Base {
private:
  int b_i;

public:
  DerivedA(int i_, int j_): Base(i_) { 
    b_i = j_;
  };

  void print() {
    std::cout<< "Class DA " << a_i << "," << b_i <<  "\n";
  }
};

void foo() {
  Base *b = new Base(5);
  Base *d = new DerivedA(5, 10); 

  b->print();
  d->print();


  DerivedA * d1 = dynamic_cast<DerivedA *> (d);
  d1->print();

  // segmentation fault
  // DerivedA * d2 = dynamic_cast<DerivedA *> (b);
  // d2->print();


  DerivedA * d2 = static_cast<DerivedA *> (b);
  d2->print();

  Base * bb = dynamic_cast<Base *> (d);
  bb->print();

  ABase * ab = new ABase(7);
  ab->print();
  //void * v = (void*) ab;
  void * v = static_cast<void*> (ab);
  
  //ABase * vv = (ABase *) v;
  ABase * vv = static_cast<ABase *> (v);
  vv->print();

}

int main() {
  foo();
  return 0;
}
