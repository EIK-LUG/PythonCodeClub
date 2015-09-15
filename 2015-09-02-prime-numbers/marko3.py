primes = [2,3]

def isprime(n):
	if n % 2 == 0:
		pass
	else:
		for i in range(2, n):
			if n % i == 0:
				break
		else:
			return True

def calcNextPrime(primes):
	iterator = primes[len(primes)-1] + 1
	while  not isprime(iterator):
		iterator += 1
	else:
		primes.append(iterator)

def showprimenumber(n):
	while len(primes) < n:
		calcNextPrime(primes)
	else:
		print primes[len(primes)-1]

showprimenumber(1000)


	




