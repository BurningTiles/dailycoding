# Solution - 12 Feb 2025

---
## [2342. Max Sum of a Pair With Equal Sum of Digits](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits)

### cpp
```cpp
class Solution {
public:
    int maximumSum(vector<int>& nums) {
        int res = -1, d_n[82] = {}; // 9 * 9

        for (int n : nums) {
            int d = 0;
            
            for (int nn = n; nn; nn /= 10)
                d += nn % 10;
            
            if (d_n[d])
                res = max(res, d_n[d] + n);
            
            d_n[d] = max(d_n[d], n);
        }
        
        return res;
    }
};
```
