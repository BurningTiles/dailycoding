# Solution - 04 Feb 2025

---
## [1800. Maximum Ascending Subarray Sum](https://leetcode.com/problems/maximum-ascending-subarray-sum)

### cpp
```cpp
class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int cur = nums[0], ans = nums[0];

        for(int i=1; i<nums.size(); ++i) {
            if(nums[i] > nums[i-1]) cur += nums[i];
            else cur = nums[i];

            ans = max(ans, cur);
        }

        return ans;
    }
};
```
