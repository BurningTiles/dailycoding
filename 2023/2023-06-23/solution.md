# Solution - 23 Jun 2023

---
## [1. Integer to Roman Numeral](https://workat.tech/problem-solving/practice/integer-to-roman) [(LeetCode)](https://leetcode.com/problems/integer-to-roman/) 

### cpp
```cpp
string integerToRoman(int num) {
	vector<int> val = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
	vector<string> ch = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
	string ans = "";
	for(int i=0; i<val.size(); i++)
		while(num>=val[i])
			num -= val[i], ans += ch[i];
	return ans;
}
```


---
## [2. Substring Search - I](https://workat.tech/problem-solving/practice/substring-search) [(LeetCode)](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) 

### cpp
```cpp
int findStartIndexOfSubstring(string s1, string s2) {
	if(s2.size()>s1.size()) return -1;
	for(int i=0; i<=s1.size()-s2.size(); i++) {
		int j=0;
		while(j<s2.size() && s1[i+j]==s2[j]) ++j;
		if(j==s2.size()) return i;
	}
	return -1;
}
```
