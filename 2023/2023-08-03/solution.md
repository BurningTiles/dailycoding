# Solution - 03 Aug 2023

---
## [1. Letter Combinations of a Phone Number](https://workat.tech/problem-solving/practice/letter-combinations-of-a-phone-number) [(LeetCode)](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) 

### cpp
```cpp
string letters[] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

void helper(string &digits, vector<string> &ans, string cur, int i=0) {
	if(i==digits.size()) { ans.push_back(cur); return; }
	for(auto &ch:letters[digits[i]-'0'])
		helper(digits, ans, cur + ch, i+1);
}

vector<string> letterCombinations(string digits) {
	vector<string> ans;
	string cur = "";
	helper(digits, ans, cur);
	return ans;
}
```
