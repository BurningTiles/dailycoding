# Solution - 13 Mar 2024

---
## [2485. Find the Pivot Integer](https://leetcode.com/problems/find-the-pivot-integer)

### cpp
```cpp
class Solution {
public:
    int pivotInteger(int n) {
        long long sum = n * (n+1) / 2, x = sqrt(sum);
        return x * x == sum ? x : -1;
    }
};
```
