# Solution - 25 Apr 2025

---
## [2845. Count of Interesting Subarrays](https://leetcode.com/problems/count-of-interesting-subarrays)

### cpp
```cpp
class Solution {
public:
    long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
        long long ans = 0, acc = 0;
        unordered_map<int, int> count;
        count[0] = 1;

        for(int n:nums) {
            acc = (acc + (n % modulo == k ? 1 : 0)) % modulo;
            ans += count[(acc-k+modulo) % modulo];
            count[acc]++;
        }

        return ans;
    }
};
```
