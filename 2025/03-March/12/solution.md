# Solution - 12 Mar 2025

---
## [2529. Maximum Count of Positive Integer and Negative Integer](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer)

### cpp
```cpp
class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int pos=0, neg=0;

        for(int i=0; i<nums.size(); ++i) {
            if(nums[i] > 0) ++pos;
            if(nums[i] < 0) ++neg;
        }

        return max(pos, neg);
    }
};
```
