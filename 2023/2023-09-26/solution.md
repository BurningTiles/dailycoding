# Solution - 26 Sep 2023

---
## [1. Rod Cutting](https://workat.tech/problem-solving/practice/rod-cutting) 

### cpp
```cpp
int maximumProfit(int n, vector<int> &prices) {
	int dp[n+1]; dp[0] = 0;
	for(int i=1; i<=n; i++) {
		dp[i] = 0;
		for(int j=1; j<=i && j<=prices.size(); j++)
			dp[i] = max(dp[i], dp[i-j] + prices[j-1]);
	}
	
	return dp[n];
}
```
