# Solution - 03 Oct 2023

---
## [1. Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs)

### cpp
```cpp
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int count[101] = {0}, ans = 0;
        for(auto &num:nums)
            ans += count[num]++;
        return ans;
    }
};
```
