# Solution - 26 Feb 2025

---
## [1749. Maximum Absolute Sum of Any Subarray](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray)

### cpp
```cpp
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int pos = 0, neg = 0, posCur = 0, negCur = 0;

        for(int i=0; i<nums.size(); ++i) {
            posCur += nums[i];
            negCur -= nums[i];
            if(posCur < 0) posCur = 0;
            if(negCur < 0) negCur = 0;
            pos = max(pos, posCur);
            neg = max(neg, negCur);
        }

        return max(pos, neg);
    }
};
```
