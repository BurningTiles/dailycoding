def power(x):
	ans = 0
	while x!=1:
		if x%2==0:
			x //= 2
		else:
			x = x*3+1
		ans += 1
	return ans

def getKth(low, high, k):
	v = []
	for i in range(low, high+1):
		v.append([power(i), i])
	v.sort()
	return v[k-1][1]

print(getKth(12, 15, 2))
print(getKth(1, 1, 1))
print(getKth(7, 11, 4))