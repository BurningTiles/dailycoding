def sqrt(n):
	ans = 1
	while abs(ans*ans-n)>0.0001:
		ans = (ans+(n/ans))/2
	return int(ans*1000)/1000

print(sqrt(5))