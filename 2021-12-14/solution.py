def max_diff(v):
	ans, minv = -1, v[0]
	for i in range(1, len(v)):
		if v[i]<=minv:
			minv = v[i]
		else:
			ans = max([ans, v[i]-minv])
	return ans

print(max_diff([7, 1, 5, 4]))
print(max_diff([9, 4, 3, 2]))
print(max_diff([1, 5, 2, 10]))