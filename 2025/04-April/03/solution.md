# Solution - 03 Apr 2025

---
## [2874. Maximum Value of an Ordered Triplet II](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii)

### cpp
```cpp
class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        long long ans = 0, a = 0, ab = 0;

        for(int i=0; i<nums.size(); ++i) {
            ans = max(ans, ab * nums[i]);
            ab = max(ab, a - nums[i]);
            a = max(a, (long long)nums[i]);
        }

        return ans;
    }
};
```
