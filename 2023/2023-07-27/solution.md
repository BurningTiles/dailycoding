# Solution - 27 Jul 2023

---
## [1. Combination Sum 1](https://workat.tech/problem-solving/practice/combination-sum-1) [(LeetCode)](https://leetcode.com/problems/combination-sum/) 

### cpp
```cpp
void helper(vector<int> &A, vector<vector<int>> &ans, vector<int> &cur, int target, int i=0) {
	if(target==0) ans.push_back(cur);
	if(target>0 && i<A.size()) {
		cur.push_back(A[i]);
		helper(A, ans, cur, target-A[i], i);
		cur.pop_back();
		helper(A, ans, cur, target, i+1);
	}
}

vector<vector<int> > combinationSum(vector<int> &A, int val) {
	vector<vector<int>> ans;
	vector<int> cur;
	helper(A, ans, cur, val);
	return ans;
}
```
