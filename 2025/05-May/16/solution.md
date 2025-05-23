# Solution - 16 May 2025

---
## [2901. Longest Unequal Adjacent Groups Subsequence II](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii)

### cpp
```cpp
class Solution {
public:
    bool differByOne(string &s1, string &s2) {
        if(s1.size() != s2.size()) return false;
        int diff = 0;
        for(int i=0; i<s1.size(); ++i) {
            diff += s1[i] != s2[i];
            if(diff > 1) return false;
        }
        return diff == 1;
    }

    vector<string> getWordsInLongestSubsequence(vector<string>& words, vector<int>& groups) {
        int n = groups.size(), maxi = 0;
        vector<pair<int, int>> dp(n, {1, -1});

        for(int i=0; i<n; ++i) {
            for(int j=i-1; j>=0; --j) {
                if(groups[i] != groups[j] 
                    && dp[i].first < dp[j].first + 1
                    && differByOne(words[i], words[j])) {
                        dp[i] = {dp[j].first + 1, j};
                }
            }
            maxi = max(maxi, dp[i].first);
        }

        vector<string> ans;

        for(int i=0; i<n; ++i) {
            if(maxi == dp[i].first) {
                while(i != -1) {
                    ans.push_back(words[i]);
                    i = dp[i].second;
                }
                break;
            }
        }
        reverse(ans.begin(), ans.end());

        return ans;
    }
};
```
