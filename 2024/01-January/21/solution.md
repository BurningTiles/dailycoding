# Solution - 21 Jan 2024

---
## [198. House Robber](https://leetcode.com/problems/house-robber)

### cpp
```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int last = 0, last2 = 0, last3 = 0, ans = 0;

        for(auto num:nums) {
            int curMax = max(num + last2, num + last3);
            ans = max(curMax, ans);
            last3 = last2, last2 = last, last = curMax;
        }

        return ans;
    }
};
```
