import math

def checkPerfectNumber(n):
	if n==1:
		return True
	sum, sq = 1, math.ceil(n**.5)
	for i in range(2, sq):
		if n%i==0:
			sum += i + n//i
	if sq*sq==n:
		sum += sq
	return sum==n

print(checkPerfectNumber(28))