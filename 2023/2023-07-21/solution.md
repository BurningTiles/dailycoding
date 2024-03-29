# Solution - 21 Jul 2023

---
## [1. Longest Substring Without Repeat](https://workat.tech/problem-solving/practice/longest-substring-without-repeat) [(LeetCode)](https://leetcode.com/problems/longest-substring-without-repeating-characters/) 

### cpp
```cpp
int longestSubstringWithoutRepeat(string s) {
	int ans = 0, j=0, count[128]={0}, curLen=0;
	for(int i=0; i<s.size(); i++) {
		while(count[s[i]]) 
			--count[s[j++]], --curLen;
		++curLen, ++count[s[i]];
		ans = max(ans, curLen);
	}
	return ans;
}
```


---
## [2. Distinct Numbers in Window](https://workat.tech/problem-solving/practice/distinct-numbers-window) 

### cpp
```cpp
vector<int> distintNumbersInWindow(vector<int> &A, int k) {
	unordered_map<int, int> um;
	for(int i=0; i<k; i++)
		um[A[i]]++;
	
	vector<int> ans = {um.size()};
	for(int i=k; i<A.size(); i++) {
		if(um[A[i-k]]>1) um[A[i-k]]--;
		else um.erase(A[i-k]);
		um[A[i]]++;
		ans.push_back(um.size());
	}
	
	return ans;
}
```
