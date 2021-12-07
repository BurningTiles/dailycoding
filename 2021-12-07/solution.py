dp = []
def calculate(i, j, k, n, m):
	if i>j or k>=len(m): return 0
	if dp[i][k]!=-1: return dp[i][k]
	dp[i][k]=max([
		n[i]*m[k]+calculate(i+1, j, k+1, n, m),
		n[j]*m[k]+calculate(i, j-1, k+1, n, m)
	])
	return dp[i][k]
def max_score(n, m):
	global dp
	dp = [[-1]*1001 for i in range(1001)]
	return calculate(0, len(n)-1, 0, n, m)

print(max_score([1, 2, 3], [3, 2, 1]))
print(max_score([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))