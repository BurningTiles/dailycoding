# Solution - 22 Oct 2023

---
## [1793. Maximum Score of a Good Subarray](https://leetcode.com/problems/maximum-score-of-a-good-subarray)

### cpp
```cpp
class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(false),cin.tie(0);
        int ans = nums[k], mn = nums[k], i = k, j = k, n = nums.size();
        while(i || j<n-1) {
            if(i==0 || (j<n-1 && nums[j+1]>nums[i-1]))
                mn = min(mn, nums[++j]);
            else
                mn = min(mn, nums[--i]);
            ans = max(ans, mn * (j-i+1));
        }
        return ans;
    }
};
```
