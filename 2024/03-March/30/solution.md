# Solution - 30 Mar 2024

---
## [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers)

### cpp
```cpp
class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        int ans = 0, n = nums.size();

        for(int l=0, m=0, r=0; r<n; ++r) {
            if(++cnt[nums[r]]==1)
                if(--k < 0) {
                    cnt[nums[m++]] = 0;
                    l = m;
                }
            if(k <= 0) {
                while(cnt[nums[m]] > 1)
                    --cnt[nums[m++]];
                ans += m - l + 1;
            }
        }

        return ans;
    }
};
```
