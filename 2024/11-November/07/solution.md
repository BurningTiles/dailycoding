# Solution - 07 Nov 2024

---
## [2275. Largest Combination With Bitwise AND Greater Than Zero](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero)

### cpp
```cpp
class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        int cnt[28] = {0}, ans = 0;

        for(int c:candidates) {
            int i=0;
            while(c) {
                cnt[i] += c&1;
                c /= 2;
                ++i;
            }
        }

        for(int i=0; i<28; ++i)
            ans = max(cnt[i], ans);
            
        return ans;
    }
};
```
