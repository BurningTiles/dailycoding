# Solution - 30 Apr 2024

---
## [1915. Number of Wonderful Substrings](https://leetcode.com/problems/number-of-wonderful-substrings)

### cpp
```cpp
class Solution {
public:
    long long wonderfulSubstrings(string word) {
        long long cnt[1024] = {1}, mask = 0, ans = 0;

        for(auto ch:word) {
            mask ^= 1 << (ch - 'a');
            ans += cnt[mask];
            
            for(int i=0; i<10; ++i)
                ans += cnt[mask ^ (1 << i)];
            
            ++cnt[mask];
        }

        return ans;
    }
};
```
