# Solution - 19 Jun 2025

---
## [2294. Partition Array Such That Maximum Difference Is K](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k)

### cpp
```cpp
class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());

        int ans = 1, last = nums[0];

        for(int i=1; i<nums.size(); ++i)
            if(nums[i] - last > k)
                ++ans, last = nums[i];

        return ans;
    }
};
```
