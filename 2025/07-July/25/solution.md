# Solution - 25 Jul 2025

---
## [3487. Maximum Unique Subarray Sum After Deletion](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion)

### cpp
```cpp
class Solution {
public:
    int maxSum(vector<int>& nums) {
        int ans = INT_MIN, sum = 0;
        unordered_set<int> used;

        for(int i=0; i<nums.size(); ++i) {
            if(nums[i] <= 0)
                ans = max(ans, nums[i]);
            else if(!used.count(nums[i])) {
                used.insert(nums[i]);
                sum += nums[i];
                ans = max(ans, sum);
            }
        }

        return ans;
    }
};
```
