# Solution - 09 Oct 2023

---
## [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)

### cpp
```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l=0, r=nums.size()-1, lw=-1, up=-1;
        while(l<=r) {
            int mid = l + (r-l)/2;
            if(target==nums[mid]) lw = mid;
            if(target<=nums[mid])
                r=mid-1;
            else
                l=mid+1;
        }
        if(lw == -1) return {-1, -1};
        
        l=0, r=nums.size()-1;
        while(l<=r) {
            int mid=l+(r-l)/2;
            if(target==nums[mid]) up = mid;
            if(nums[mid]<=target)
                l=mid+1;
            else
                r=mid-1;
        }

        return {lw, up};
    }
};
```
