# Solution - 30 Nov 2023

---
## [1611. Minimum One Bit Operations to Make Integers Zero](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero)

### cpp
```cpp
class Solution {
public:
    int minimumOneBitOperations(int n) {
        int ans;
        for(ans = 0; n > 0; n &= n-1)
            ans = -(ans + (n ^ (n-1)));
        return abs(ans);
    }
};
```
