# Solution - 06 May 2025

---
## [1920. Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation)

### cpp
```cpp
class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        int n = nums.size();

        for(int i=0; i<n; ++i)
            nums[i] = nums[i] + (n * (nums[nums[i]] % n));
        
        for(int i=0; i<n; ++i)
            nums[i] /= n;
        
        return nums;
    }
};
```
