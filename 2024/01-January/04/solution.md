# Solution - 04 Jan 2024

---
## [2870. Minimum Number of Operations to Make Array Empty](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty)

### cpp
```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_map<int, int> um;
        for(auto num:nums) ++um[num];

        int ans = 0;
        for(auto [val, count]: um) {
            if(count == 1) return -1;
            ans += count / 3;
            if(count % 3) ++ans;
        }

        return ans;
    }
};
```
