# Solution - 06 Oct 2023

---
## [1. Integer Break](https://leetcode.com/problems/integer-break/) 

### cpp
```cpp
class Solution {
public:
    int integerBreak(int n) {
        if(n<=3) return n-1;
        int ans=1;
        while(n>4) 
            ans *= 3, n -= 3;
        return ans * n;
    }
};
```
