# Solution - 15 May 2025

---
## [2900. Longest Unequal Adjacent Groups Subsequence I](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i)

### cpp
```cpp
class Solution {
public:
    vector<string> getLongestSubsequence(vector<string>& words, vector<int>& groups) {
        vector<string> ans;
        int last = -1;

        for(int i=0; i<words.size(); ++i) {
            if(last != groups[i]) {
                ans.push_back(words[i]);
                last = groups[i];
            }
        }

        return ans;
    }
};
```
