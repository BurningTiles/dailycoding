# Solution - 01 Jun 2025

---
## [2929. Distribute Candies Among Children II](https://leetcode.com/problems/distribute-candies-among-children-ii)

### cpp
```cpp
class Solution {
public:
    long long h3(long long n) {
        return n<0 ? 0 : (n+1)*(n+2)/2;
    }

    long long distributeCandies(int n, int limit) {
        return h3(n) - 3LL * h3(n-limit-1) + 3LL * h3(n-2*(limit+1)) - h3(n-3*(limit+1));
    }
};
```
