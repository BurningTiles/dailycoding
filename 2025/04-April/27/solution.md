# Solution - 27 Apr 2025

---
## [3392. Count Subarrays of Length Three With a Condition](https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition)

### cpp
```cpp
class Solution {
public:
    int countSubarrays(vector<int>& nums) {
        int ans = 0;

        for(int i=1; i<nums.size()-1; ++i)
            if(!(nums[i]&1) && nums[i]/2 == nums[i-1] + nums[i+1])
                ++ans;

        return ans;
    }
};
```
