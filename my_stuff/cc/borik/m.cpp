#include "TransformationItem.h"
#include <typeinfo>
#include <iostream> 

using namespace cdp::cdpp;
using namespace std;

int main() {
  TransformationItem * t = new TransformationItem(4);
  cout << "Type name: "<< typeid(*t).name() << endl; 
  int s = t->getSize();

}
