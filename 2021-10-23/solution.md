# Concatenated Words

### Python
```python
class Solution:
	def findAllConcatenatedWordsInAList(self, words):
		wordsSet = set()
		for word in words: wordsSet.add(word)
		ans = []
		
		def canBreak(s):
			if not wordsSet or not s: return False
			dp = [False]* ( len(s) + 1)
			dp[0] = True
			for i in range(0, len(s)):
				for j in range(i + 1, len(s) + 1):
					if dp[i] and s[i: j] in wordsSet:
						dp[j] = True
			return dp[len(s)]
		
		for word in words:
			wordsSet.remove(word)
			if canBreak(word): ans.append(word)
			wordsSet.add(word)
		return ans

input = ["tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"]
print(Solution().findAllConcatenatedWordsInAList(input))
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

bool canBreak(string s, set<string> &wordsSet){
	if(!wordsSet.size() or !s.size()) return false;
	vector<bool> dp(s.size()+1, false);
	dp[0] = true;
	for(int i=0; i<s.size(); i++)
		for(int j=i+1; j<=s.size(); j++)
			if(dp[i] && wordsSet.count(s.substr(i, j-i)))
				dp[j] = true;
	return dp[s.size()];
}

vector<string> findAllConcatenatedWordsInAList(vector<string> words){
	vector<string> ans;
	set<string> wordsSet;
	for(auto word:words)
		wordsSet.insert(word);
	for(auto word:words){
		wordsSet.erase(word);
		if(canBreak(word, wordsSet))
			ans.push_back(word);
		wordsSet.insert(word);
	}
	return ans;
}

void print(vector<string> v){
	cout << "[";
	for(int i=0; i<v.size(); i++)
		cout << "\"" << v[i] << "\"" << (i==v.size()-1 ? "" : ", ");
	cout << "]" << endl;
}

signed main() {
	print(findAllConcatenatedWordsInAList({"tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"}));
	return 0;
}
```