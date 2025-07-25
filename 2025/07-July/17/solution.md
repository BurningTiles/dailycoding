# Solution - 17 Jul 2025

---
## [3202. Find the Maximum Length of Valid Subsequence II](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii)

### cpp
```cpp
class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        int ans = 2;
        vector<int> dp(nums.size(), 0);

        for(int kk=0; kk<k; ++kk) {
            vector<int> dp(k, 0);

            for(int i=0; i<nums.size(); ++i) {
                int mod = nums[i] % k;
                int pos = (kk-mod+k) % k;
                dp[mod] = dp[pos] + 1;
            }

            ans = max(ans, *max_element(dp.begin(), dp.end()));
        }

        return ans;
    }
};
```
