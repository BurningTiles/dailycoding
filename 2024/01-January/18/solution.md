# Solution - 18 Jan 2024

---
## [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs)

### cpp
```cpp
class Solution {
public:
    int climbStairs(int n) {
        int a=1, b=1;
        
        while(--n)
            a = (b += a) - a;

        return b;
    }
};
```
