def fibonacci(n):
	if n<2: return n
	a, b, c = 0, 1, 1
	while n>1:
		n -= 1
		c = a+b
		a = b
		b = c
	return c

print(fibonacci(9))