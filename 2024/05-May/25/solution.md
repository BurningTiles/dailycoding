# Solution - 25 May 2024

---
## [140. Word Break II](https://leetcode.com/problems/word-break-ii)

### cpp
```cpp
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> words(wordDict.begin(), wordDict.end());
        vector<string> ans;
        helper(s, words, ans);
        return ans;
    }

    void helper(string &s, unordered_set<string> &words, vector<string> &ans, string cur="", int i=0) {
        if(i==s.size())
            ans.push_back(cur);

        if(cur.size()) 
            cur.push_back(' ');
        string word = "";

        for(int j=i; j<s.size(); ++j) {
            word.push_back(s[j]);
            if(words.count(word))
                helper(s, words, ans, cur + word, j+1);
        }
    }
};
```
