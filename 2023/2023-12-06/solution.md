# Solution - 06 Dec 2023

---
## [1716. Calculate Money in Leetcode Bank](https://leetcode.com/problems/calculate-money-in-leetcode-bank)

### cpp
```cpp
class Solution {
public:
    int totalMoney(int n) {
        int d = n/7, r = n%7;
        int ans = (28 * 2 + 7 * (d-1)) * d / 2;
        if(r) ans += r * (d*2 + r + 1) / 2;
        return ans;
    }
};
```
