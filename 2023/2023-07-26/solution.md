# Solution - 26 Jul 2023

---
## [1. Subsets - II](https://workat.tech/problem-solving/practice/subsets-ii) [(LeetCode)](https://leetcode.com/problems/subsets-ii/) 

### cpp
```cpp
void generate(vector<int> &A, vector<vector<int>> &ans, vector<int> &cur, int i=0) {
	if(i==A.size()) { ans.push_back(cur); return; }
	int j = i+1;
	while(j<A.size() && A[j]==A[j-1]) ++j;
	generate(A, ans, cur, j);
	cur.push_back(A[i]);
	generate(A, ans, cur, i+1);
	cur.pop_back();
}

vector<vector<int> > subsets(vector<int> &A) {
	sort(A.begin(), A.end());
	vector<vector<int>> ans;
	vector<int> cur;
	generate(A, ans, cur);
	return ans;
}
```


---
## [2. Subset Sum](https://workat.tech/problem-solving/practice/subset-sum) 

### cpp
```cpp
bool hasValidSubset(vector<int> &A, int target) {
	int n = A.size();
	bool dp[n+1][target+1];
	
	for(int j=0; j<=target; j++) dp[0][j] = false;
	for(int i=0; i<=n; i++) dp[i][0] = true;
	
	for(int i=1; i<=n; i++)
		for(int j=1; j<=target; j++) 
			if(j-A[i-1]>=0)
				dp[i][j] = dp[i-1][j-A[i-1]] || dp[i-1][j];
			else
				dp[i][j] = dp[i-1][j];
	
	return dp[n][target];
}

/*
// Another approach.
bool hasValidSubset(vector<int> &A, int target, int i=0) {
	if(target==0) return true;
	if(i==A.size()) return false;
	if(hasValidSubset(A, target, i+1)) return true;
	return hasValidSubset(A, target-A[i], i+1);
}
*/
```
