import sys

def collatz(n):
	while True:
		if n%2 == 0:
			n = n//2
		else:
			n = 3*n + 1
		yield n

dict = {}
currentLargestLength = 0
currentLargestStart = 0
for n in range(int(sys.argv[1]), 2, -1): 
	c = collatz(n)
	count = 1
	while True:
		k = int(next(c))
		if k == 1:
			break
		if k in dict.keys():
			count += int(dict[k])
			break
		else:
			count += 1
	if count > currentLargestLength:
		currentLargestLength = count
		currentLargestStart = n
	dict[n] = count

print(currentLargestStart)
