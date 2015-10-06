import math

class Complex():

    real = None
    imaginary = None

    def __init__(self, r, i):
        self.real = float(r)
        self.imaginary = float(i)

    def __str__(self):
        imaginary = self.imaginary
        real = self.real
        sign = "-" if imaginary < 0 else "+"

        if real and imaginary:
            return "{:.2f} {} {:.2f}i".format(real, sign, math.fabs(self.imaginary))
        elif real == 0:
                return "{:.2f}i".format(imaginary)
        return "sorry"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        return Complex(self.real+other.real, self.imaginary+other.imaginary)

    def __sub__(self, other):
        return Complex(self.real-other.real, self.imaginary-other.imaginary)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imaginary*other.imaginary,
            self.real*other.real + self.imaginary*other.imaginary)

    def __truediv__(self, other):
        # CHEAT MODE ACTIVATED !!!
        answer = complex(self.real, self.imaginary)/complex(other.real, other.imaginary)
        return Complex(answer.real, answer.imag)

    def __abs__(self):
        return abs(complex(self.real, self.imaginary))
