# Solution - 03 Feb 2025

---
## [3105. Longest Strictly Increasing or Strictly Decreasing Subarray](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray)

### cpp
```cpp
class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int inc=1, dec=1, ans = 1;
        
        for(int i=1; i<nums.size(); ++i) {
            if(nums[i] > nums[i-1])
                ++inc, dec = 1;
            else if(nums[i] < nums[i-1]) 
                ++dec, inc = 1;
            else
                dec = inc = 1;
            ans = max(ans, max(inc, dec));
        }

        return ans;
    }
};
```
