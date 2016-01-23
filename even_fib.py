import sys

def fib():
	a, b = 0, 1
	while True:
		c = a + b
		a = b
		b = c
		if a % 2 == 0:
			yield a

f = fib()
total = 0

while True:
	n = int(next(f))
	if n > 4 * 10**6:
		break
	else:
		total += n

print(total)
