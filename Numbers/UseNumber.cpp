#include <iostream>
#include "Number.h"
#include "Number.cpp"

// To test compile erros
int main() {
  Number num(128401);

  std::cout << "My Number: " << num << '\n';

  return 0;
}
