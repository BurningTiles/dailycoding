# Solution - 11 Sep 2024

---
## [2220. Minimum Bit Flips to Convert Number](https://leetcode.com/problems/minimum-bit-flips-to-convert-number)

### cpp
```cpp
class Solution {
public:
    int minBitFlips(int start, int goal) {
        int ans = 0;

        while(start || goal) {
            if((start&1) != (goal&1))
                ++ans;
            start >>= 1, goal >>= 1;
        }

        return ans;
    }
};
```
