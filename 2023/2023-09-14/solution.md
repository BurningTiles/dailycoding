# Solution - 14 Sep 2023

---
## [1. Longest Increasing Subsequence (LIS)](https://workat.tech/problem-solving/practice/longest-increasing-subsequence) [(LeetCode)](https://leetcode.com/problems/longest-increasing-subsequence/) 

### cpp
```cpp
int getLengthOfLIS(vector<int> &A) {
	vector<int> v(A.size());
	v[0] = 1;
	int ans = 1;
	for(int i=1; i<A.size(); i++){
		v[i] = 1;
		for(int j=i-1; j>=0; j--)
			if(A[i]>A[j])
				v[i] = max(v[i], v[j]+1);
		ans = max(v[i], ans);
	}
	return ans;
}
```
