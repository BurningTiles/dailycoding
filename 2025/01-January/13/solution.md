# Solution - 13 Jan 2025

---
## [3223. Minimum Length of String After Operations](https://leetcode.com/problems/minimum-length-of-string-after-operations)

### cpp
```cpp
class Solution {
public:
    int minimumLength(string s) {
        int cnt[26] = {0}, ans = 0;

        for(char ch:s)
            cnt[ch-'a']++;
        
        for(int i=0; i<26; ++i)
            if(cnt[i])
                ans += cnt[i]&1 ? 1 : 2;
        
        return ans;
    }
};
```
