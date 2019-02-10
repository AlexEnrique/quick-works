#ifndef NUMBER_CPP_
#define NUMBER_CPP_
#include <deque>
#include <sstream>
#include <string>

#include "Number.h"

typedef unsigned int uint;

// Constructor
Number::Number(uint number) {
  uint digit = 0;
  uint decimalPlace = 10;

  while (number != 0) {
    /*
      - Why the " / (decimalPlace / 10)"?
      Note:
        > 124515 % 10 == 5
        > 124510 % 100 == 10
        ...
      To get the digit, we devided by the (decimalPlace / 10)
    */
    digit = (number % decimalPlace) / (decimalPlace / 10);
    this->_digits.push_front(digit);

    number -= number % decimalPlace; // remove at the right position
    decimalPlace *= 10;
  }
}

// Operators
Number::operator const char*() const {
  std::ostringstream output;
  for (auto iElement = _digits.begin(); iElement < _digits.end(); ++iElement) {
    output << *iElement;
  }

  return (output.str()).c_str();
}

void Number::operator=(const Number& cpSource) {
  if (cpSource._digits.size() > 0) {
    for (auto iElement = cpSource._digits.begin(); iElement < cpSource._digits.end(); ++iElement) {
      this->_digits.push_back(*iElement);
    }
  }
}

void Number::operator=(int number) {
  uint castedNumber = static_cast<uint>((number >= 0) ? number : -number);
  Number aux(castedNumber);

  *this = aux;
}

void Number::operator=(uint number) {
  Number aux(number);
  *this = aux;
}

Number& Number::operator++() { // TODO: Rewrite it more simple
  size_t length = this->_digits.size();
  uint i = static_cast<uint>(length - 1); // position index

  if (length > 0) {
    while (i > -1) {
      this->_digits[i] += 1;
      if (this->_digits[i] == 10) {
        this->_digits[i] = 0;
        i -= 1; // go to the next index to increment it
      }
      else
        break;
    }

    if (this->_digits[0] == 0)
      this->_digits.push_front(1);
  }
  else // if length <= 0
    this->_IncrementOperatorException();
}

Number Number::operator++(int) { // TODO: Rewrite it more simple
  Number copy = *this;
  ++(*this);

  return copy;
}

Number& Number::operator--() {
  size_t length = this->_digits.size();
  uint i = static_cast<uint>(length - 1); // position index

  if (length > 0) {
    while (i > -1) {
      this->_digits[i] -= 1;
      if (this->_digits[i] == -1) {
        this->_digits[i] = 0;
        i -= 1; // go to the next index to increment it
      }
      else
        break;
    }

    // Check if the first digit is zero. If so, iterate thru the array until
    // find a non zero number, popping the most significative digits.
    for (auto iElement = this->_digits.begin(); (*iElement == 0 || iElement < this->_digits.end()); ++iElement) {
      this->_digits.pop_front();
    }
  }
  else // if length <= 0
    this->_DecrementOperatorException();
}

Number Number::operator--(int) {
  Number copy = *this;
  --(*this);

  return copy;
}


// Methods
void Number::_IncrementOperatorException() const {
  std::ostringstream errMessage;
  errMessage << "Number::operator++() error: the size of the Number was zero.";
  errMessage << '\n';
  errMessage << "Possibly the Number has not been initialized";

  throw errMessage.str();
}

void Number::_DecrementOperatorException() const {
  std::ostringstream errMessage;
  errMessage << "Number::operator--() error: the size of the Number was zero.";
  errMessage << '\n';
  errMessage << "Possibly the Number has not been initialized";

  throw errMessage.str();
}

inline size_t Number::GetNumberOfDigits() const {
  return this->_digits.size();
}

#endif
