# Solution - 08 Apr 2025

---
## [3396. Minimum Number of Operations to Make Elements in Array Distinct](https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct)

### cpp
```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        bool cnt[101] = {0};
        
        for(int i=nums.size()-1; i>=0; --i) {
            if(cnt[nums[i]])
                return (i+3)/3;
            cnt[nums[i]] = true;
        }

        return 0;
    }
};
```
