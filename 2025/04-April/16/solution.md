# Solution - 16 Apr 2025

---
## [2537. Count the Number of Good Subarrays](https://leetcode.com/problems/count-the-number-of-good-subarrays)

### cpp
```cpp
class Solution {
public:
    long long countGood(vector<int>& nums, int k) {
        long long ans = 0;

        unordered_map<int, int> count;

        for(int i=0, j=0; j<nums.size(); ++j) {
            k -= count[nums[j]]++;

            while(k <= 0)
                k += --count[nums[i++]];
            
            ans += i;
        }

        return ans;
    }
};
```
