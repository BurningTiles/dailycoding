# Solution - 22 Sep 2023

---
## [1. Subset Sum 2](https://workat.tech/problem-solving/practice/subset-sum-2) 

### cpp
```cpp
int subsetSum(vector<int> &A, int target) {
	int n = A.size();
	bool dp[n+1][target+1];
	for(int i=0; i<=target; i++) dp[0][i] = 0;
	for(int i=0; i<=n; i++) dp[i][0] = true;
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=target; j++) {
			dp[i][j] = dp[i-1][j];
			if(j>=A[i-1]) 
				dp[i][j] |= dp[i-1][j-A[i-1]];
		}
	}
	return dp[n][target];
}
```
