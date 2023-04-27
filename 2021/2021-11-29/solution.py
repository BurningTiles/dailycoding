def num_ways(n, m):
	a = [[0]*(m+1) for _ in range(n+1)]
	a[0][1] = 1
	for i in range(1, n+1):
		for j in range(1, m+1):
			a[i][j] = a[i][j-1] + a[i-1][j]
	return a[n][m]

print (num_ways(2, 2))
print (num_ways(3, 7))