# Solution - 01 Aug 2023

---
## [1. Tug of War](https://workat.tech/problem-solving/practice/tug-of-war) [(LeetCode)](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/) 

### cpp
```cpp
void helper(vector<int> &A, int &ans, int &total, int sum = 0, int i=0, int n=0) {
	if(i==A.size()) return;
	if(n==A.size()/2) ans = min(ans, abs(total-sum*2));
	else {
		helper(A, ans, total, sum, i+1, n);
		helper(A, ans, total, sum+A[i], i+1, n+1);
	}
}

int divideGroup(vector<int> &A) {
	int ans = INT_MAX, total = 0;
	for(auto &x:A) total += x;
	helper(A, ans, total);
	return ans;
}
```
