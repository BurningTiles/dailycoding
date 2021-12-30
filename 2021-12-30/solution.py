def smallestIntDivByK(k):
	if k%2==0 or k%5==0: return -1
	n, l = 1, 1
	while n%k:
		n = (n*10+1)%k
		l += 1
	return l

print(smallestIntDivByK(1))
print(smallestIntDivByK(2))
print(smallestIntDivByK(3))