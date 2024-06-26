# Solution - 21 Jun 2024

---
## [1052. Grumpy Bookstore Owner](https://leetcode.com/problems/grumpy-bookstore-owner)

### cpp
```cpp
class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        auto satisfied = 0, maxExtraSatisfied = 0, extraSatisfied = 0;
        for (auto i = 0; i < customers.size(); ++i) {
            satisfied += !grumpy[i] * customers[i];
            extraSatisfied += grumpy[i] * customers[i];
            if (i >= minutes)
                extraSatisfied -= grumpy[i - minutes] * customers[i - minutes];
            
            maxExtraSatisfied = max(maxExtraSatisfied, extraSatisfied);
        }
        return satisfied + maxExtraSatisfied;
    }
};
```
