def pow(x, n):
	ans = 1
	while n:
		if n&1: ans = ans*x if n>0 else ans/x
		x *= x
		n //= 2
	return ans

print(pow(5, 3))