# Solution - 29 Nov 2023

---
## [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits)

### cpp
```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        while(n){
            ans += n&1;
            n /= 2;
        }
        return ans;
    }
};
```
