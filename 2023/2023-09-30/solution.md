# Solution - 30 Sep 2023

---
## [1. 132 Pattern](https://leetcode.com/problems/132-pattern/) 

### cpp
```cpp
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int c = INT_MIN;
        stack<int> stk;
        for(int i=nums.size()-1; i>=0; --i) {
            if(nums[i]<c) return true;
            while(stk.size() && nums[i]>stk.top())
              c = stk.top(), stk.pop();
            stk.push(nums[i]);
        }
        return false;
    }
};
```
