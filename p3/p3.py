import math

def is_prime(primes, num):
	term = 0
	while term < math.sqrt(num):
		term = primes.pop(0)
		if num%term == 0:
			return False
	return True

target = 600851475143
primes = [2]
factors = []
i = 3

while i <= target:
	if is_prime(list(primes), i):
		primes.append(i)
		if target%i == 0:
			target = target / i
			factors.append(i)
	i += 2

print factors.pop()
