# Solution - 23 Oct 2023

---
## [342. Power of Four](https://leetcode.com/problems/power-of-four)

### cpp
```cpp
class Solution {
public:
    bool isPowerOfFour(int n) {
        return n>0 && !(n&(n-1)) && n%3==1;
    }
};
```
