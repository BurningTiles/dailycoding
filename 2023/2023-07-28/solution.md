# Solution - 28 Jul 2023

---
## [1. Combination Sum 2](https://workat.tech/problem-solving/practice/combination-sum-2) [(LeetCode)](https://leetcode.com/problems/combination-sum-ii/) 

### cpp
```cpp
void helper(vector<int> &A, vector<vector<int>> &ans, vector<int> &cur, int target, int i=0) {
	if(target==0) { ans.push_back(cur); return; }
	for(int j=i; j<A.size(); j++) {
		if(A[j]>target || (j>i && A[j]==A[j-1])) continue;
		cur.push_back(A[j]);
		helper(A, ans, cur, target-A[j], j+1);
		cur.pop_back();
	}
}

vector<vector<int> > combinationSum(vector<int> &A, int val) {
	sort(A.begin(), A.end());
	vector<vector<int>> ans;
	vector<int> cur;
	
	helper(A, ans, cur, val);
	return ans;
}
```
