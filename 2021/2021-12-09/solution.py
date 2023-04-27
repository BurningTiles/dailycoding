def min_diff(n, k):
	n.sort()
	ans, k = n[-1]-n[0], k-1
	for i in range(k,len(n)):
		ans = min([ans, n[i]-n[i-k]])
	return ans

print(min_diff([90], 1))
print(min_diff([9, 4, 1, 7], 2))