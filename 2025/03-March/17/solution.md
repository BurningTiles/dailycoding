# Solution - 17 Mar 2025

---
## [2206. Divide Array Into Equal Pairs](https://leetcode.com/problems/divide-array-into-equal-pairs)

### cpp
```cpp
class Solution {
public:
    bool divideArray(vector<int>& nums) {
        int cnt[501] = {0};

        for(int i=0; i<nums.size(); ++i)
            ++cnt[nums[i]];

        for(int i=0; i<501; ++i)
            if(cnt[i]&1)
                return false;

        return true;
    }
};
```
