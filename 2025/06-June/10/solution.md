# Solution - 10 Jun 2025

---
## [3442. Maximum Difference Between Even and Odd Frequency I](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i)

### cpp
```cpp
class Solution {
public:
    int maxDifference(string s) {
        int cnt[26] = {0}, odd=0, even=100;

        for(auto ch:s)
            cnt[ch-'a']++;
        
        for(int i=0; i<26; ++i)
            if(cnt[i]&1)
                odd = max(odd, cnt[i]);
            else if(cnt[i] > 0)
                even = min(even, cnt[i]);

        return odd-even;
    }
};
```
