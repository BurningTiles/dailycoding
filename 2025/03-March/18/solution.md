# Solution - 18 Mar 2025

---
## [2401. Longest Nice Subarray](https://leetcode.com/problems/longest-nice-subarray)

### cpp
```cpp
class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int AND = 0, i = 0, ans = 0, n = nums.size();

        for(int j=0; j<n; ++j) {
            while((AND & nums[j]) > 0)
                AND ^= nums[i++];
            AND |= nums[j];
            ans = max(ans, j-i+1);
        }

        return ans;
    }
};
```
