#ifndef NUMBER_CPP_
#define NUMBER_CPP_
#include <deque>
#include <sstream>
#include <string>
#include <cstdint>
#include <exception>
#include <stdlib.h>

#include "Number.h"

typedef unsigned int uint;

// Constructor
Number::Number() {} // TODO: implement it ??

Number::Number(std::uint64_t number) {
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

Number::Number(const char* input) {
  std::string str(input);

  for (char& c : str) {
    int digit = static_cast<int>(c) - 48;
    this->_digits.push_back(digit); // this for read the string from the left
  }
}

Number::Number(const std::string& input) {
  for (char& c : const_cast<std::string&>(input)) {
    int digit = static_cast<int>(c) - 48;
    this->_digits.push_front(digit);
  }
}

Number::Number(const Number& cpSource) { // TODO: Need this?
  if (cpSource._digits.size() > 0) {
    for (auto iElement = cpSource._digits.begin(); iElement < cpSource._digits.end(); ++iElement) {
      this->_digits.push_back(*iElement);
    }
  }
}


// Methods
void Number::_IncrementOperatorException() const {
  std::ostringstream errMessage;
  errMessage << "Number::operator++() error: the size of the Number was zero.";
  errMessage << "Possibly the Number has not been initialized";

  std::cout << '\n' << errMessage.str() << '\n';

  std::bad_alloc exc;
  throw exc;
}

void Number::_DecrementOperatorException() const {
  std::ostringstream errMessage;
  errMessage << "Number::operator--() error: the size of the Number was zero.";
  errMessage << "Possibly the Number has not been initialized";

  std::cout << '\n' << errMessage.str() << '\n';

  std::bad_alloc exc;
  throw exc;
}

void Number::_GetSmallerDigitsDeque(const Number& first, const Number& second, std::deque<uint>& smaller) {
  smaller = ( first.GetNumberOfDigits() < second.GetNumberOfDigits() ? first._digits : second._digits );
}

void Number::_GetGreaterDigitsDeque(const Number& first, const Number& second, std::deque<uint>& greater) {
  greater = ( first.GetNumberOfDigits() > second.GetNumberOfDigits() ? first._digits : second._digits );
}


inline size_t Number::GetNumberOfDigits() const {
  return this->_digits.size();
}


// Operators
Number::operator const char*() const {
  char* output = (char*)malloc(sizeof(char) * (this->_digits.size() + 1));

  for (int i = 0; i < this->_digits.size(); ++i) {
    output[i] = static_cast<char>(this->_digits.at(i) + 48);
  }
  output[this->_digits.size()] = '\0';

  return static_cast<const char*>(output);
}

void Number::operator=(const Number& cpSource) {
  this->_digits = cpSource._digits;
}

void Number::operator=(int number) {
  uint castedNumber = static_cast<uint>((number >= 0) ? number : -number);
  Number aux(castedNumber);

  *this = aux;
}

void Number::operator=(uint number) {
  Number aux(static_cast<std::uint64_t>(number));
  *this = aux;
}

void Number::operator=(std::uint64_t number) {
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

Number Number::operator++(int) {
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

Number Number::operator+(const Number& other) {
  // get the greatest length:
  size_t length = std::max(this->GetNumberOfDigits(), other.GetNumberOfDigits());
  bool differentSize = this->GetNumberOfDigits() != other.GetNumberOfDigits();

  std::deque<uint> greater, smaller; // get the greater as smaller *._digits
                                     // if they are the same size, the order
                                     // does not matter (see below).
  // initializing the greater and smaller std::deque<uint>:
  if (differentSize) {
    Number::_GetSmallerDigitsDeque(*this, other, smaller);
    Number::_GetGreaterDigitsDeque(*this, other, greater);

    while (smaller.size() < greater.size())
      smaller.push_front(0);
  } else {
    smaller = this->_digits;
    greater = other._digits;
  }

  // Calculating the sum:
  Number result;       // the result to be returned
  uint   sum     = 0;  // The sum of the digits in the current position
  uint   remaind = 0;  // remaind = sum - (sum % 10); if sum >= 10, remaind = 1.
                       // the remaind (remainder) will be added to the next digit
  for (int i = length - 1; i > -1; --i) { // start summing from the end
    sum = smaller[i] + greater[i];
    result._digits.push_front((sum % 10) + remaind);  // (sum % 10) <= 8

    remaind = ((sum > 9) ? 1 : 0);
    sum = 0;
  }

  // if the last sum (first digit from the left) was greater than 10, create
  // a new digit and set it to 1
  if (remaind == 1)
    result._digits.push_front(1);

  return result;
}

Number Number::operator+(std::uint64_t n) {
  Number aux(n);
  return (*this) + aux;
}

// Number Number::operator*(const Number& other) { // TODO: Implement it
  // // get the greatest length:
  // size_t length = std::max(this->GetNumberOfDigits(), other.GetNumberOfDigits());
  // bool differentSize = this->GetNumberOfDigits() != other.GetNumberOfDigits();
  //
  // std::deque<uint> greater, smaller; // get the greater as smaller *._digits
  //                                    // if they are the same size, the order
  //                                    // does not matter (see below).
  // // initializing the greater and smaller std::deque<uint>:
  // if (differentSize) {
  //   Number::_GetSmallerDigitsDeque(*this, other, smaller);
  //   Number::_GetGreaterDigitsDeque(*this, other, greater);
  //
  //   while (smaller.size() < greater.size())
  //     smaller.push_front(0);
  // } else {
  //   smaller = this->_digits;
  //   greater = other._digits;
  // }
  //
  // // Calculating the sum:
  // Number result;       // the result to be returned
  // uint   prod    = 1;  // The sum of the digits in the current position
  // uint   remaind = 0;  // remaind = sum - (sum % 10); if sum >= 10, remaind = 1.
  //                      // the remaind (remainder) will be added to the next digit
  // for (int i = length - 1; i > -1; --i) { // start summing from the end
  //   prod = smaller[i] * greater[i]; // 0 <= prod <= 81
  //   result._digits.push_front((prod + remaind) % 10);
  //
  //   if (prod + remaind > 10) {
  //     remaind = prod - ((prod + remaind) % 10);
  //     remaind /= 10;
  //   } else {
  //     remaind = 0;
  //   }
  //   prod = 1;
  // }
  //
  // // if the last sum (first digit from the left) was greater than 10, create
  // // a new digit and set it to 1
  // if (remaind != 0)
  //   result._digits.push_front(remaind);
  // std::cout << "Number::operator*(): remaind == " << remaind << '\n';
  //
  // return result;
}

Number Number::operator*(std::uint64_t n) {
  Number aux(n);
  return (*this) * aux;
}

void Number::operator+=(const Number& other) {
  *this = *this + other;
}

void Number::operator+=(std::uint64_t n) {
  Number aux(n);
  *this += aux;
}

void Number::operator*=(const Number& other) {
  *this = *this * other;
}

void Number::operator*=(std::uint64_t n) {
  Number aux(n);
  *this *= aux;
}

bool Number::operator==(const Number& other) const {
  if (this->_digits.size() != other._digits.size())
    return false;
  else {
    auto iThis  = this->_digits.begin();
    auto iOther = other._digits.begin();

    while (iThis < this->_digits.end()) {
      if (*iThis == *iOther) {
        ++iThis;
        ++iOther;
      }
      else
        return false;
    }
  }

  return true;
}

bool Number::operator!=(const Number& other) const {
  return !(*this == other);
}

// bool Number::operator>(const Number& other) const;
// bool Number::operator<(const Number& other) const;

// bool Number::operator>=(const Number& other) const;
// bool Number::operator<=(const Number& other) const;

uint Number::operator[](int i) const {
  return this->_digits.at(i);
}

uint Number::operator[](int i) {
  return this->_digits.at(i);
}














#endif
