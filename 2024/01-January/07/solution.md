# Solution - 07 Jan 2024

---
## [446. Arithmetic Slices II - Subsequence](https://leetcode.com/problems/arithmetic-slices-ii-subsequence)

### cpp
```cpp
#define ll long long
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        vector<unordered_map<ll, int>> dp(nums.size());
        int ans = 0;

        for(int i=1; i<nums.size(); ++i) {
            for(int j=0; j<i; ++j) {
                ll diff = (ll) nums[i] - nums[j], tmp = dp[j][diff];
                dp[i][diff] += tmp + 1;
                ans += tmp;
            }
        }

        return ans;
    }
};
```
