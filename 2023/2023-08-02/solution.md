# Solution - 02 Aug 2023

---
## [1. String Permutations](https://workat.tech/problem-solving/practice/string-permutations) [(LeetCode)](https://leetcode.com/problems/permutations/) 

### cpp
```cpp
void helper(string &s, vector<string> &ans, int i=0) {
	if(i==s.size()) { ans.push_back(s); return; }
	for(int j=i; j<s.size(); j++) {
		swap(s[i], s[j]);
		helper(s, ans, i+1);
		swap(s[i], s[j]);
	}
}

vector<string> getAllPermutations(string s) {
	vector<string> ans;
	helper(s, ans);
	return ans;
}
```
