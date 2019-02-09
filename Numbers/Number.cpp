#ifndef NUMBER_CPP_
#define NUMBER_CPP_
#include <deque>
#include <cstdint>
#include "Number.h"
#include <sstream>
#include <string>

typedef unsigned int uint;
// Constructor
Number::Number(uint number) {
  uint digit = 0;
  uint decimalPlace = 10;

  while (number != 0) {
    /*
      - Why the  / (decimalPlace / 10)?
      Note:
        > 124515 % 10 == 5
        > 124510 % 100 == 10
        ...
      To get the digit, we devided by the (decimalPlace / 10)
    */
    digit = (number % decimalPlace) / (decimalPlace / 10);
    this->_digits.push_front(digit);

    decimalPlace *= 10;
    number -= number % decimalPlace; // remove at the right position
  }
}

// TODO: Change this to '=' operator
// Number::Number(const Number& cpSource) {
//   if (cpSource._digits.size() > 0) {
//     for (auto iElement = cpSource._digits.begin(); iElement < cpSource._digits.end(); ++iElement) {
//       this->_digits.push_back(*iElement);
//     }
//   }
// }

// Operators
operator const char*() const {
  std::ostringstream output = "";
  for (auto iElement = _digits.begin(); iElement < _digits.end(); ++iElement) {
    output << *iElement;
  }

  return (output.str()).c_str();
}

#endif
