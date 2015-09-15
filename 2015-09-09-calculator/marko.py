class Calculator:
		
	def __init__(self):
		self.tehe = []
		self.result = 0
		self.multiplications = 0
		self.divisions = 0
		self.operators = ['+','-','*','/']

	def breakdown(self, input_string):
		operators = self.operators
		temp = ""
		tehe = self.tehe

		for x in input_string:
			if x in operators:
				try:
					tehe.append(float(temp))
				except ValueError:
					pass	
				tehe.append(x)
				temp = ""
			else:
				temp += x
		tehe.append(float(temp))

		self.multiplications = tehe.count('*')
		self.divisions = tehe.count('/')

	def multiplyDivide(self):
		position = 0
		tehe = self.tehe
		multiplications = self.multiplications
		divisions = self.divisions
		special = ['*','/']

		while multiplications > 0:
			position = tehe.index('*')
			if tehe[position-2] not in special:
				korrutis = tehe[position-1] * tehe[position+1]
				del tehe[position-1:position+2]
				tehe.insert(position-1,korrutis)
				multiplications -= 1
			else:
				position = tehe.index('/')
				if tehe[position-2] not in special:
					jagatis = tehe[position-1] / tehe[position+1]
					del tehe[position-1:position+2]
					tehe.insert(position-1,jagatis)
					divisions -= 1	

		while divisions > 0:
			position = tehe.index('/')
			if tehe[position-2] not in special:
				jagatis = tehe[position-1] / tehe[position+1]
				del tehe[position-1:position+2]
				tehe.insert(position-1,jagatis)
				divisions -= 1
			else:
				pass

	def addSubtract(self):
		tehe = self.tehe
		operators = self.operators
		position = 0

		while len(tehe) > 0:
			for x in tehe:
				if x not in operators:
					position = tehe.index(x)
					if position == 0:
						self.result += x
						del tehe[0]
					elif tehe[position-1] == "+":
						self.result += x
						del tehe[position-1:position+1]
					elif tehe[position-1] == "-":
						self.result -= x
						del tehe[position-1:position+1]

	def calculate(self, input_string):

		self.breakdown(input_string)
		self.multiplyDivide()
		self.addSubtract()		
		return self.result