#include <iostream>
#include "Number.h"
#include "Number.cpp"
#include <cstdint>
#include <cmath>


// To test compile erros
int main() {
  Number num1("47");
  Number num2(3);

  // std::cout << "num1 * num2: " << num1 * num2 << '\n'; // ans: 141

  // std::cout << sizeof(uint64_t) << std::endl; // 8 bytes
  // std::cout << sizeof(int) << std::endl;      // 4 bytes
  // std::cout << static_cast<int>(std::abs(std::remainder(14, 8))) << '\n';


  return 0;
}
