# Solution - 10 Oct 2023

---
## [2009. Minimum Number of Operations to Make Array Continuous](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous)

### cpp
```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int maxlen = 1, n = nums.size();
        sort(nums.begin(),nums.end());
        nums.erase(unique(nums.begin(),nums.end()),nums.end());
        
        for(int i=1, j=0; i<nums.size(); ++i) {
            while(nums[i]-nums[j] >= n) ++j;
            maxlen = max(maxlen, i-j+1);
        }
        
        return n - maxlen;
    }
};
```
