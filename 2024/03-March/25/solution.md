# Solution - 25 Mar 2024

---
## [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array)

### cpp
```cpp
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ans;
        
        for(auto &x:nums) {
            int i = abs(x)-1;
            if(nums[i] < 0) ans.push_back(abs(x));
            else nums[i] = -nums[i];
        }

        return ans;
    }
};
```
