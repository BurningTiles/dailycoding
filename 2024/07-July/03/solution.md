# Solution - 03 Jul 2024

---
## [1509. Minimum Difference Between Largest and Smallest Value in Three Moves](https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves)

### cpp
```cpp
class Solution {
public:
    int minDifference(vector<int>& nums) {
        if(nums.size() <= 4) return 0;
        sort(nums.begin(), nums.end());

        int ans = INT_MAX;
        for(int i=0, k=nums.size()-4; i<=3; ++i)
            ans = min(ans, nums[i+k] - nums[i]);

        return ans;
    }
};
```
