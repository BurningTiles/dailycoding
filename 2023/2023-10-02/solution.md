# Solution - 02 Oct 2023

---
## [1. Maximum Product Subarray](https://workat.tech/problem-solving/practice/max-product-subarray) [(LeetCode)](https://leetcode.com/problems/maximum-product-subarray) 

### cpp
```cpp
int maxProduct(vector<int> &A) {
	long long ans = INT_MIN, cur = 1;
	for(int i=0; i<A.size(); ++i) {
		cur *= A[i];
		if(cur > ans) ans = cur;
		if(!A[i]) cur = 1;
	}
	cur = 1;
	for(int i=A.size()-1; i>-1; --i) {
		cur *= A[i];
		if(cur > ans) ans = cur;
		if(!A[i]) cur = 1;
	}
	return ans;
}
```
