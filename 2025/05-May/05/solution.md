# Solution - 05 May 2025

---
## [790. Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling)

### cpp
```cpp
class Solution {
public:
    int numTilings(int n) {
        int a = 0, b = 1, c = 1, tmp, mod = 1e9+7;

        while(--n) {
            tmp = (c * 2 % mod + a) % mod;
            a = b, b = c, c = tmp;
        }

        return c;
    }
};
```
