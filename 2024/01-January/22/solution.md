# Solution - 22 Jan 2024

---
## [645. Set Mismatch](https://leetcode.com/problems/set-mismatch)

### cpp
```cpp
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int duplicate = 0;

        for(auto num:nums) {
            int i = abs(num) - 1;
            if(nums[abs(num)-1] < 0) duplicate = abs(num);
            else nums[i] = -nums[i];
        }
        
        for(int i=0; i<nums.size(); ++i)
            if(nums[i] > 0)
                return {duplicate, i+1};
        return {};
    }
};
```
