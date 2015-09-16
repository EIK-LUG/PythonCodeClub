import unittest
from complex import Complex
 
 
class TestComplexNumbers(unittest.TestCase):
 
    def test_normal(self):
        x = Complex(1, 3)
 
        self.assertEqual(str(x), "1.00 + 3.00i", "Complex number 1.00 + 3.00i doesn't print the correct value")
 
    def test_zero_real(self):
        x = Complex(0, 15)
 
        self.assertEqual(str(x), "15.00i", "Complex number 15.00i doesn't print the correct value")
 
    def test_negative_imaginary(self):
        x = Complex(1.539, -2.5)
 
        self.assertEqual(str(x), "1.54 - 2.50i", "Complex number 1.539 - 2.50i doesn't print the correct value")
 
    def test_negative_imaginary_with_zero_real(self):
        x = Complex(0, -999)
 
        self.assertEqual(str(x), "-999.00i", "Complex number -999.00i doesn't print the correct value")
 
    def test_both_negative(self):
        x = Complex(-10, -20)
 
        self.assertEqual(str(x), "-10.00 - 20.00i", "Complex number -10.00 - 20.00i doesn't print the correct value")
 
 
if __name__ == '__main__':
    unittest.main()
