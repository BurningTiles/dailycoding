# Solution - 24 Apr 2024

---
## [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number)

### cpp
```cpp
class Solution {
public:
    int tribonacci(int n) {
        int v[38] = {0,1,1};

        for(int i=3; i<=n; ++i)
            v[i] = v[i-1] + v[i-2] + v[i-3];
            
        return v[n];
    }
};
```
