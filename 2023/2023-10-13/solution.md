# Solution - 13 Oct 2023

---
## [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs)

### cpp
```cpp
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size(), dp[n];
        dp[0] = cost[0], dp[1] = cost[1];
        for(int i = 2; i < n; i++)
            dp[i] = cost[i] + min(dp[i-1], dp[i-2]);
        return min(dp[n-2], dp[n-1]);
    }
};
```
