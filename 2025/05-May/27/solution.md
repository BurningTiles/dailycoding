# Solution - 27 May 2025

---
## [2894. Divisible and Non-divisible Sums Difference](https://leetcode.com/problems/divisible-and-non-divisible-sums-difference)

### cpp
```cpp
class Solution {
public:
    int differenceOfSums(int n, int m) {
        int sum1 = n * (n + 1) / 2, sum2 = (n/m) * (m + m * (n/m)) / 2;
        return sum1 - sum2 * 2;
    }
};
```
