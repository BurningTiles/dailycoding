# Solution - 14 Jun 2024

---
## [945. Minimum Increment to Make Array Unique](https://leetcode.com/problems/minimum-increment-to-make-array-unique)

### cpp
```cpp
class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int ans = 0;

        for(int i=1; i<nums.size(); ++i)
            if(nums[i] <= nums[i-1])
                ans += nums[i-1] + 1 - nums[i],
                nums[i] = nums[i-1] + 1;
        
        return ans;
    }
};
```
