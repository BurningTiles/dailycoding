# Solution - 02 Apr 2025

---
## [2873. Maximum Value of an Ordered Triplet I](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i)

### cpp
```cpp
class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        long long ans = 0;
        int maxa = 0, maxab = 0;

        for(int i=0; i<nums.size(); ++i){
            ans = max(ans, 1LL * maxab * nums[i]);
            maxab = max(maxab, maxa-nums[i]);
            maxa = max(maxa, nums[i]);
        }

        return ans;
    }
};
```
