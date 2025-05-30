# Solution - 23 May 2025

---
## [3068. Find the Maximum Sum of Node Values](https://leetcode.com/problems/find-the-maximum-sum-of-node-values)

### cpp
```cpp
class Solution {
public:
    // After drawing few trees understood we can freely change any even number of nodes in tree.

    long long maximumValueSum(vector<int>& nums, int k, vector<vector<int>>& edges) {
        long long sum = 0, cnt = 0, sacrifice = INT_MAX;
        
        for(long long n:nums) {
            sum += max(n ^ k, n);
            cnt += (n ^ k) > n;
            sacrifice = min(sacrifice, abs(n - (n ^ k)));
        }
        
        return sum - (cnt&1 ? sacrifice : 0);
    }
};
```
