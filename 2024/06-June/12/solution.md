# Solution - 12 Jun 2024

---
## [75. Sort Colors](https://leetcode.com/problems/sort-colors)

### cpp
```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int l=0, r=nums.size()-1;
        
        for(int i=0; i<=r; ++i) {
            if(nums[i]==0 && i != l)
                swap(nums[i--], nums[l++]);
            else if(nums[i]==2 && i != r)
                swap(nums[i--], nums[r--]);
        }
    }
};
```
