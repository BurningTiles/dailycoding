# Solution - 23 Nov 2023

---
## [1630. Arithmetic Subarrays](https://leetcode.com/problems/arithmetic-subarrays)

### cpp
```cpp
class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        vector<bool> ans;
        for(int i=0; i<l.size(); ++i)   
            ans.push_back(isArithmetic(nums, l[i], r[i]));
        return ans;
    }

    bool isArithmetic(vector<int> &nums, int l, int r) {
        int mn=INT_MAX, mx=INT_MIN;
        for(int i=l; i<=r; ++i) {
            if(nums[i]<mn) mn=nums[i];
            if(nums[i]>mx) mx=nums[i];
        }

        if(mn==mx) return true;
        if((mx-mn)%(r-l)) return false;

        int diff = (mx-mn)/(r-l), index;
        vector<bool> mark(r-l+1, false);

        for(int i=l; i<=r; ++i) {
            if((nums[i]-mn) % diff) return false;
            index = (nums[i]-mn) / diff;
            
            if(mark[index]) return false;
            mark[index] = true;
        }
        
        return true;
    }
};
```
