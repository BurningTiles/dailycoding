# Solution - 19 Feb 2024

---
## [231. Power of Two](https://leetcode.com/problems/power-of-two)

### cpp
```cpp
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && ! (n & n-1);
    }
};
```
