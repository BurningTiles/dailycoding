# Solution - 23 Jul 2024

---
## [1636. Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency)

### cpp
```cpp
class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int, int> cnt;
        
        for(auto num:nums) ++cnt[num];

        sort(nums.begin(), nums.end(), [&](const int &a, const int &b) {
            return cnt[a] == cnt[b] ? a > b : cnt[a] < cnt[b];
        });

        return nums;
    }
};
```
