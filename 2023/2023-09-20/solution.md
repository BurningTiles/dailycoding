# Solution - 20 Sep 2023

---
## [1. Edit Distance (Levenshtein Distance)](https://workat.tech/problem-solving/practice/edit-distance) [(LeetCode)](https://leetcode.com/problems/edit-distance/description/) 

### cpp
```cpp
int minOperations(string s1, string s2) {
	int n=s1.size(), m=s2.size(), v[m+1], pre, cur;
	for(int i=0; i<=m; ++i) v[i] = i;
	for(int i=1; i<=n; ++i) {
		pre = v[0], v[0] = i;
		for(int j=1; j<=m; ++j) {
			cur = v[j];
			if(s1[i-1]==s2[j-1]) v[j] = pre;
			else v[j] = 1 + min(pre, min(cur, v[j-1]));
			pre = cur;
		}
	}
	return v[m];
}
```
