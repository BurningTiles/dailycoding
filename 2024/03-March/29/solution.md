# Solution - 29 Mar 2024

---
## [2962. Count Subarrays Where Max Element Appears at Least K Times](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times)

### cpp
```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        long long mx = *max_element(nums.begin(), nums.end());
        long long left = 0, right = 0, ans = 0, cnt = 0, n = nums.size();

        while(right < n) {
            if(nums[right] == mx) ++cnt;

            while(cnt >= k) {
                if(nums[left] == mx) --cnt;
                ++left;
                ans += n-right;
            }

            ++right;
        }

        return ans;
    }
};
```
