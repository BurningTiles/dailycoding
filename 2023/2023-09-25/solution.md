# Solution - 25 Sep 2023

---
## [1. Maximum path sum in matrix](https://workat.tech/problem-solving/practice/max-path-sum-matrix) 

### cpp
```cpp
int findMaxPath(vector<vector<int>> &M) {
	int n=M.size(), m=M[0].size(), ans=0;
	int dp[n+1][m+2];
	for(int i=0; i<=n; i++) dp[i][0] = dp[i][m+1] = 0;
	for(int i=0; i<m+2; i++) dp[0][i] = 0;
	
	for(int i=1; i<=n; i++)
		for(int j=1; j<=m; j++) {
			dp[i][j] = max({ dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1] }) 
				+ M[i-1][j-1];
			ans = max(ans, dp[i][j]);
		}
	
	return ans;
}
```
