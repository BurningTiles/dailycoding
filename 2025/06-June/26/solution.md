# Solution - 26 Jun 2025

---
## [2311. Longest Binary Subsequence Less Than or Equal to K](https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k)

### cpp
```cpp
class Solution {
public:
    int longestSubsequence(string s, int k) {
        long long i=s.size()-1, value=0LL, mul=1;
        while(i >= max(0, int(s.size())-32)) {
            if(s[i] == '1') value += mul;
            if(value > k) break;
            mul *= 2, i--;
        }

        int ans=0;
        for(int j=0; j<s.size(); ++j)
            if(!(s[j]=='1' && j<=i))
                ++ans;
        
        return ans;
    }
};
```
