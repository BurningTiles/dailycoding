# Solution - 17 Jun 2024

---
## [633. Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers)

### cpp
```cpp
class Solution {
public:
    bool judgeSquareSum(int c) {
        long long limit = sqrt(c), l=0, r=limit;

        while(l<=r) {
            long long sum = l*l + r*r;
            if(sum == c)
                return true;
            sum > c ? --r : ++l;
        }

        return false;
    }
};
```
