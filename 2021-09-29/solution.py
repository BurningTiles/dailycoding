def shortest_dist(s, ch):
	n = len(s)
	ans = [int(1e9)]*n
	for i in range(n):
		if s[i]==ch:
			ans[i] = 0
	for i in range(n):
		if ans[i]==0:
			j, dist=i-1, 1
			while j>=0 and ans[j]>dist:
				ans[j] = dist
				j -= 1
				dist += 1
			dist = 1
			j=i+1
			while j<n and ans[j]>dist:
				ans[j] = dist
				j += 1
				dist += 1
	return ans

print(shortest_dist('helloworld', 'l'))