# Solution - 19 Nov 2024

---
## [2461. Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k)

### cpp
```cpp
class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long long ans = 0, curSum = 0;
        unordered_map<int, int> umap;

        for(int i=0,j=0; i<nums.size(); ++i) {
            curSum += nums[i];
            umap[nums[i]]++;

            if(i >= k-1) {
                if(umap.size() == k)
                    ans = max(ans, curSum);
                curSum -= nums[j];
                if(--umap[nums[j]] == 0)
                    umap.erase(nums[j]);
                ++j;
            }
        }

        return ans;
    }
};
```
