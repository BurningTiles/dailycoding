# Solution - 02 May 2024

---
## [2441. Largest Positive Integer That Exists With Its Negative](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative)

### cpp
```cpp
class Solution {
public:
    int findMaxK(vector<int>& nums) {
        int cnt[1001] = {0}, ans = -1;
        
        for(int i=0; i<nums.size(); ++i)
            if(cnt[abs(nums[i])] && cnt[abs(nums[i])] != nums[i])
                ans = max(ans, abs(nums[i]));
            else cnt[abs(nums[i])] = nums[i];

        return ans;
    }
};
```
