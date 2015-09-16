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

