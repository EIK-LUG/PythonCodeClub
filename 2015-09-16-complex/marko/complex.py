class Complex:
	real = None
	imaginary = None
	a = None
	b = None
	c = None
	d = None

	def __init__(self,r,i):
		self.real = float(r)
		self.imaginary = float(i)

	def __str__(self):
	
		if self.real ==0.0:
			return "%.2fi" % self.imaginary
		elif self.imaginary < 0:
			return "%.2f - %.2fi" % (self.real,-self.imaginary)
		else:
			return "%.2f + %.2fi" % (self.real,self.imaginary)

	def __repr__(self):
		return str(self)

	def __add__(self, other):
		return Complex(self.real + other.real, self.imaginary + other.imaginary)

	def __sub__(self,other):
		return Complex(self.real - other.real, self.imaginary - other.imaginary)

	def __mul__(self,other):
		return Complex(((self.real * other.real) - (self.imaginary*other.imaginary)), ((self.real * other.imaginary) + (self.imaginary*other.real)))	

	def __div__(self, other):
		self.a = self.real
		self.b = self.imaginary
		self.c = other.real
		self.d = other.imaginary

		return Complex(((self.a*self.c)+(self.b*self.d))/((self.c*self.c)+(self.d*self.d)), ((self.b*self.c)-(self.a*self.d))/((self.c*self.c)+(self.d*self.d)))