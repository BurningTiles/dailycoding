# Solution - 26 Jun 2023

---
## [1. Longest Common Prefix](https://workat.tech/problem-solving/practice/longest-common-prefix) [(LeetCode)](https://leetcode.com/problems/longest-common-prefix/) 

### cpp
```cpp
string longestCommonPrefix(vector<string> &str) {
	string ans = str[0];
	for(auto &s:str) {
		int i=0;
		while(i<s.size() && i<ans.size() && s[i]==ans[i]) ++i;
		ans = ans.substr(0,i);
	}
	return ans;
}
```


---
## [2. Anagrams](https://workat.tech/problem-solving/practice/anagrams) 

### cpp
```cpp
bool areAnagrams(string A, string B) {
	int count[128] = {0};
	for(auto &ch:A)
		count[ch]++;
	for(auto &ch:B)
		count[ch]--;
	for(auto &c:count)
		if(c!=0) return false;
	return true;
}
```
