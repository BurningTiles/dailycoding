# Solution - 12 Jun 2025

---
## [3423. Maximum Difference Between Adjacent Elements in a Circular Array](https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array)

### cpp
```cpp
class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int ans = abs(nums.front() - nums.back());

        for(int i=1; i<nums.size(); ++i)
            ans = max(ans, abs(nums[i] - nums[i-1]));

        return ans;
    }
};
```
