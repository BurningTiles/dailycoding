# Solution - 05 Oct 2023

---
## [1. Majority Element II](https://leetcode.com/problems/majority-element-ii) 

### cpp
```cpp
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int val1 = 0, val2 = 1, count1 = 0, count2 = 0;
        for(auto &num:nums) {
            if(num==val1) ++count1;
            else if(num==val2) ++count2;
            else if(count1==0) val1=num, count1=1;
            else if(count2==0) val2=num, count2=1;
            else --count1, --count2;
        }
        count1 = count2 = 0;
        for(auto &num:nums)
            if(num==val1) ++count1;
            else if(num==val2) ++count2;
        
        vector<int> ans;
        if(count1>nums.size()/3) ans.push_back(val1);
        if(count2>nums.size()/3) ans.push_back(val2);
        return ans;
    }
};
```
