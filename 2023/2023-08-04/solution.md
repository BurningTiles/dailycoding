# Solution - 04 Aug 2023

---
## [1. Generate Parentheses](https://workat.tech/problem-solving/practice/generate-parentheses) [(LeetCode)](https://leetcode.com/problems/generate-parentheses/) 

### cpp
```cpp
void helper(vector<string> &ans, string cur, int n, int open=0, int close=0) {
	if(cur.size()==(n<<1)) { ans.push_back(cur); return; }
	if(open<n) helper(ans, cur+"(", n, open+1, close);
	if(close<open) helper(ans, cur+")", n, open, close+1);
}

vector<string> generateParentheses(int n) {
	vector<string> ans;
	helper(ans, "", n);
	return ans;
}
```
