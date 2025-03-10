# Solution - 04 Jan 2025

---
## [1930. Unique Length-3 Palindromic Subsequences](https://leetcode.com/problems/unique-length-3-palindromic-subsequences)

### cpp
```cpp
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        vector<pair<int, int>> v(26, {-1, -1});
        for(int i=0; i<s.size(); i++)
            if(v[s[i]-'a'].first == -1) v[s[i]-'a'].first = i;
            else v[s[i]-'a'].second = i;

        int ans = 0;
        for(int i=0; i<26; i++) {
            if(v[i].first == -1 || v[i].second == -1) continue;
            ans += countUnique(s, v[i].first+1, v[i].second-1);
        }
        
        return ans;
    }

    int countUnique(string &s, int i, int j) {
        bool mark[128] = {0};
        int ans = 0;
        while(i<=j && ans<26) {
            if(!mark[s[i]]) 
                ++ans, mark[s[i]] = true;
            i++;
        }
        return ans;
    }
};
```
