# Solution - 27 Sep 2023

---
## [1. Coin Change](https://workat.tech/problem-solving/practice/coin-change) 

### cpp
```cpp
int numberOfCombinations(vector<int> &coins, int target) {
	int n = coins.size(), dp[n+1][target+1];
	for(int i=0; i<=target; i++) dp[0][i] = 0;
	for(int i=0; i<=n; i++) dp[i][0] = 1;
	
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=target; j++) {
			dp[i][j] = dp[i-1][j];
			if(j>=coins[i-1]) dp[i][j] += dp[i][j-coins[i-1]];
		}
	}
	
	return dp[n][target];
}
```
