# Solution - 22 Jul 2025

---
## [1695. Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value)

### cpp
```cpp
class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_map<int, int> umap;
        int ans = 0, sum = 0;

        for(int i=0, j=0; i<nums.size(); ++i) {
            sum += nums[i];
            while(umap[nums[i]]) {
                umap[nums[j]]--;
                sum -= nums[j++];
            }
            umap[nums[i]]++;
            ans = max(ans, sum);
        }

        return ans;
    }
};
```
