# Solution - 31 May 2024

---
## [260. Single Number III](https://leetcode.com/problems/single-number-iii)

### cpp
```cpp
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        long arrxor = 0;

        for(int i=0; i<nums.size(); ++i)
            arrxor ^= nums[i];
        
        arrxor &= -arrxor;
        int a = 0, b = 0;
        
        for(int i=0; i<nums.size(); ++i)
            if(nums[i] & arrxor)
                a ^= nums[i];
            else
                b ^= nums[i];
        
        return {a, b};
    }
};
```
