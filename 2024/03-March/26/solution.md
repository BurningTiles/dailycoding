# Solution - 26 Mar 2024

---
## [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive)

### cpp
```cpp
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        for(int i=0; i<nums.size(); ++i)
            while(nums[i] > 0 && nums[i] <= nums.size() && nums[nums[i]-1] != nums[i])
                swap(nums[i], nums[nums[i]-1]);
        
        for(int i=0; i<nums.size(); ++i)
            if(nums[i] != i+1)
                return i+1;
        
        return nums.size() + 1;
    }
};
```
