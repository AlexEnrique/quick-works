#ifndef NUMBER_H_
#define NUMBER_H_
#include <deque>
#include <cstdint>
#include <exception>
#include <string>
#include <stdlib.h>

typedef unsigned int uint;

class Number {
private:
  std::deque<uint> _digits;

  // Private methods
  void _IncrementOperatorException() const;
  void _DecrementOperatorException() const;
  static void _GetSmallerDigitsDeque(const Number&, const Number&, std::deque<uint>&);
  static void _GetGreaterDigitsDeque(const Number&, const Number&, std::deque<uint>&);

public:
  // Constructors and destructor
  // WARNING: Remember that the first digit must be non zero -- Handle this...

  Number();
  Number(std::uint64_t number);
  Number(const char*);
  Number(const std::string&);
  Number(const Number&); // ??TODO: Remove later?? Copy constructor
  // !!! WARNING: NOT USING A POINTER ANYMORE !!!
  // Number(const Number&); // ??TODO: Remove later?? Copy constructor
  // Number(uint numberOfDigits); // ??TODO: Remove later??

  // operators
  operator const char*() const;

  void operator=(const Number&);
  void operator=(int);
  void operator=(uint);
  void operator=(std::uint64_t);

  Number& operator++();
  Number operator++(int);

  Number& operator--();
  Number operator--(int);

  Number operator+(const Number&);
  Number operator+(std::uint64_t);

  // Number operator-(const Number&);
  // Number operator-(std::uint64_t);

  Number operator*(const Number&);
  Number operator*(std::uint64_t);

  // Number operator/(const Number&);
  // Number operator/(std::uint64_t);

  void operator+=(const Number&);
  void operator+=(std::uint64_t);

  // void operator-=(const Number&);
  // void operator-=(std::uint64_t);

  void operator*=(const Number&);
  void operator*=(std::uint64_t);

  // void operator/=(const Number&);
  // void operator/=(std::uint64_t);

  bool operator==(const Number&) const;
  bool operator!=(const Number&) const;

  bool operator>(const Number&) const;
  bool operator<(const Number&) const;

  bool operator>=(const Number&) const;
  bool operator<=(const Number&) const;

  uint operator[](int) const;
  uint operator[](int);

  // methods
  inline size_t GetNumberOfDigits() const;
};

#endif
