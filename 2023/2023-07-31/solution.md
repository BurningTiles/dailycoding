# Solution - 31 Jul 2023

---
## [1. Combinations](https://workat.tech/problem-solving/practice/combinations) [(LeetCode)](https://leetcode.com/problems/combinations/) 

### cpp
```cpp
void helper(vector<vector<int>> &ans, vector<int> &cur, int &n, int &k, int i=1, int j=0) {
	if(j==k) { ans.push_back(cur); return; }
	++j;
	for(; i<=n; i++) {
		cur.push_back(i);
		helper(ans, cur, n, k, i+1, j);
		cur.pop_back();
	}
}

vector<vector<int>> combinations(int n, int k) {
	vector<vector<int>> ans;
	vector<int> cur;
	
	helper(ans, cur, n, k);
	
	return ans;
}
```
