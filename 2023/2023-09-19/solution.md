# Solution - 19 Sep 2023

---
## [1. Longest Palindromic Substring (LPS)](https://workat.tech/problem-solving/practice/longest-palindromic-substring) [(LeetCode)](https://leetcode.com/problems/longest-palindromic-substring/) 

### cpp
```cpp
string lps(string s) {
	int n = s.size(), maxLen = 0, index=0;
	for(int i=0; i<n; ++i) {
		int l=i-1, r=i+1, len;
		while(l>=0 && r<n && s[l]==s[r]) --l, ++r;
		len = r-l-1;
		if(len > maxLen)
			maxLen = len, index = l+1;
		
		l=i, r=i+1;
		while(l>=0 && r<n && s[l]==s[r]) --l, ++r;
		len = r-l-1;
		if(len > maxLen)
			maxLen = len, index = l+1;
	}
	return s.substr(index, maxLen);
}
```
