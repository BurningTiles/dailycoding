# Solution - 03 Mar 2025

---
## [2161. Partition Array According to Given Pivot](https://leetcode.com/problems/partition-array-according-to-given-pivot)

### cpp
```cpp
class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> ans(nums.size(), pivot);

        for(int i=0, j=nums.size()-1, l=0, r=nums.size()-1; i<nums.size(); ++i, --j) {
            if(nums[i] < pivot) ans[l++] = nums[i];
            if(nums[j] > pivot) ans[r--] = nums[j];
        }

        return ans;
    }
};
```
