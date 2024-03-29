# Solution - 29 Sep 2023

---
## [1. Unique Paths](https://workat.tech/problem-solving/practice/unique-paths) 

### cpp
```cpp
#define MOD 1000000007
int uniquePaths(int m, int n) {
	long long dp[m+1][n+1];
	for(int i=0; i<=m; ++i) dp[i][0] = 0;
	for(int i=0; i<=n; ++i) dp[0][i] = 0;
	dp[0][1] = 1;
	for(int i=1; i<=m; i++)
		for(int j=1; j<=n; j++)
			dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD;
	return dp[m][n];
}

/*
// Other solution. will not work for large values.
int uniquePaths(int m, int n) {
	long long ans = 1, r = m+n-2;
	for(int i=1; i<min(m,n); i++)
		ans *= r--, ans /= i;
	return ans;
}
*/
```
