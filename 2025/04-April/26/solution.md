# Solution - 26 Apr 2025

---
## [2444. Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds)

### cpp
```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long ans = 0, bad = -1, mn = -1, mx = -1, n = nums.size();

        for(int i=0; i<n; ++i) {
            if(nums[i] < minK || nums[i] > maxK) bad = i;
            if(nums[i] == minK) mn = i;
            if(nums[i] == maxK) mx = i;
            ans += max(0LL, min(mn, mx) - bad);
        }

        return ans;
    }
};
```
