# Solution - 18 Sep 2023

---
## [1. Maximum Sum Increasing Subsequence](https://workat.tech/problem-solving/practice/maximum-sum-increasing-subsequence) 

### cpp
```cpp
int maxSumSubsequence(vector<int> &arr) {
	int n = arr.size(), dp[n], ans=0;
	for(int i=0; i<n; i++) {
		dp[i] = arr[i];
		for(int j=i-1; j>=0; --j)
			if(arr[j]<=arr[i]) 
				dp[i] = max(dp[i], dp[j] + arr[i]);
		ans = max(ans, dp[i]);
	}
	return ans;
}
```
