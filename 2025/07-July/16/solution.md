# Solution - 16 Jul 2025

---
## [3201. Find the Maximum Length of Valid Subsequence I](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i)

### cpp
```cpp
class Solution {
public:
    int maximumLength(vector<int>& nums) {
        int lastOdd = 0, lastEven = 0, fullEven = 0, fullOdd = 0;

        for(int i=0; i<nums.size(); ++i) {
            if(nums[i] & 1) {
                if(lastEven + 1 > lastOdd)
                    lastOdd = lastEven + 1;
                fullOdd += 1;
            }
            else {
                if(lastOdd + 1 > lastEven)
                    lastEven = lastOdd + 1;
                fullEven += 1;
            }
        }

        return max(max(lastOdd, lastEven), max(fullEven, fullOdd));
    }
};
```
