# Solution - 05 Mar 2025

---
## [2579. Count Total Number of Colored Cells](https://leetcode.com/problems/count-total-number-of-colored-cells)

### cpp
```cpp
class Solution {
public:
    long long coloredCells(int n) {
        vector<long long> v(n+1);
        v[0] = 0, v[1] = 1;

        for(int i=2; i<=n; ++i)
            v[i] = v[i-1] + 4 + (4*(i-2));
        
        return v[n];
    }
};
```
