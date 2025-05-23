# Solution - 07 Apr 2025

---
## [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum)

### cpp
```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for(auto &n:nums) sum += n;

        if(sum % 2 != 0) return false;

        sum /= 2;

        vector<bool> dp(sum + 1, false);
        dp[0] = true;

        for(int i=0; i<nums.size(); ++i) {
            for(int j=sum; j>=nums[i]; --j) {
                dp[j] = dp[j] || dp[j-nums[i]];
                if (dp[sum]) return true;
            }
        }

        return false;
    }
};
```
