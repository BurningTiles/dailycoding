# Solution - 25 Apr 2024

---
## [2370. Longest Ideal Subsequence](https://leetcode.com/problems/longest-ideal-subsequence)

### cpp
```cpp
class Solution {
public:
    int longestIdealString(string s, int k) {
        int cnt[26] = {0}, n = s.size(), ans = 0, cur = 0, val;

        for(int i=0; i<n; ++i) {
            cur = 1, val = s[i]-97;

            for(int j=max(0, val-k); j<=min(25, val+k); ++j)
                cur = max(cur, cnt[j] + 1);

            ans = max(ans, cur);
            cnt[val] = cur;
        }

        return ans;
    }
};
```
