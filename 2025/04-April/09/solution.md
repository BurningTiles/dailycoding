# Solution - 09 Apr 2025

---
## [3375. Minimum Operations to Make Array Values Equal to K](https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k)

### cpp
```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());

        if(nums[0] < k) return -1;

        int ans = nums[0]>k;
        for(int i=nums.size()-2; i>=0; --i) {
            if(nums[i] != nums[i+1])
                ++ans;
        }

        return ans;
    }
};
```
