# Solution - 15 Sep 2023

---
## [1. Longest Common Subsequence (LCS)](https://workat.tech/problem-solving/practice/longest-common-subsequence) 

### cpp
```cpp
int getLengthOfLCS(string s1, string s2) {
	vector<int> v1(s2.size()+1, 0), ans(s2.size()+1);
	for(int i=0; i<s1.size(); i++) {
		ans[0] = 0;
		for(int j=1; j<=s2.size(); j++)
			ans[j] = (s1[i]==s2[j-1] ? v1[j-1] + 1 : max(ans[j-1], v1[j]));
		v1 = ans;
	}
	return ans.back();
}
```
