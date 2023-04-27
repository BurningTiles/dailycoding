def integer_break(n):
	if n<4: return n-1
	ans = 1
	while n>0:
		if n==4 or n==2: return ans*n
		ans *= 3
		n -= 3
	return ans

print(integer_break(10))