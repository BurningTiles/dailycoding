# Solution - 01 Mar 2025

---
## [2460. Apply Operations to an Array](https://leetcode.com/problems/apply-operations-to-an-array)

### cpp
```cpp
class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        for (int i = 0, j = 0; i < nums.size(); ++i) {
            if (i+1 < size(nums) && nums[i] == nums[i+1])
                nums[i] *= 2, nums[i + 1] = 0;
            
            if(nums[i]) swap(nums[j++], nums[i]);
        }

        return nums;
    }
};
```
