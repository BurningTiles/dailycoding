# Solution - 28 Oct 2023

---
## [1. Word Break](https://workat.tech/problem-solving/practice/word-break) 

### cpp
```cpp
bool wordBreak (string s, vector<string> &w) {
	unordered_map<string, bool> um;
	for(auto &word:w) um[word] = true;
	vector<bool> dp(s.size()+1, false);
	dp[0] = true;
	for(int i=1; i<=s.size(); i++) {
		for(int j=i-1; j>=0; j--) {
			if(dp[j] && um[s.substr(j, i-j)]){
				dp[i] = true;
				break;
			}
		}
	}
	return dp[s.size()];
}
```
