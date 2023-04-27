def addDigits(n):
	while n>9:
		tmp = 0
		while n>0:
			tmp += n%10
			n //= 10
		n = tmp
	return n

print(addDigits(159))