# Solution - 19 Mar 2025

---
## [3191. Minimum Operations to Make Binary Array Elements Equal to One I](https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i)

### cpp
```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n=nums.size(), ans=0;

        for(int i=0; i<n-2; ++i) {
            if(nums[i] == 0) {
                nums[i] ^= 1;
                nums[i+1] ^= 1;
                nums[i+2] ^= 1;
                ++ans;
            }
        }

        return !(nums[n-1] && nums[n-2] && nums[n-3]) ? -1 : ans;
    }
};
```
