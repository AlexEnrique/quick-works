#ifndef NUMBER_H_
#define NUMBER_H_
#include <deque>
#include <cstdint>

typedef unsigned int uint;

class Number {
private:
  std::deque<uint8_t> _digits;

public:
  // Constructors and destructor
  // WARNING: Remember that the first digit must be non zero

  // !!! NOT USING A POINTER ANYMORE !!!
  // Number(); // ??TODO: Remove later??
  Number(uint number);
  // Number(const Number&); // ??TODO: Remove later?? Copy constructor
  // Number(Number&&); // ??TODO: Remove later?? Copy constructor
  // Number(uint numberOfDigits); // ??TODO: Remove later??

  // operators
  operator const char*() const;

  void operator=(const Number&);
  void operator=(int);
  void operator=(uint);

  Number& operator++();
  Number operator++(int);

  Number& operator--();
  Number operator--(int);

  void operator+=(uint);
  void operator-=(uint);

  bool operator==(const Number&) const;
  bool operator!=(const Number&) const;

  bool operator>(const Number&) const;
  bool operator<(const Number&) const;

  bool operator>=(const Number&) const;
  bool operator<=(const Number&) const;

  uint8_t operator[](int) const;
  uint8_t operator[](int);

  // methods
  uint GetNumberOfDigits() const;
};

#endif
