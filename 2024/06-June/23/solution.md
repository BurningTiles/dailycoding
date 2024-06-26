# Solution - 23 Jun 2024

---
## [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit)

### cpp
```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        multiset<int> m;
        int j = 0, ans = 1;

        for(int i=0; i<nums.size(); ++i) {
            m.insert(nums[i]);

            while(!m.empty() && *m.rbegin() - *m.begin() > limit)
                m.erase(m.find(nums[j++]));
            
            ans = max(ans, i-j+1);
        }

        return ans;
    }
};
```
