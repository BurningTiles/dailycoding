# Solution - 14 Oct 2023

---
## [2742. Painting the Walls](https://leetcode.com/problems/painting-the-walls)

### cpp
```cpp
class Solution {
public:
    int paintWalls(vector<int>& cost, vector<int>& time) {
        int n=cost.size();
        vector<int> dp(n+1, 1e9);
        dp[0] = 0;
        for (int i=0; i<n; i++)
            for (int j=n; j>0; --j)
                dp[j] = min(dp[j], dp[max(j-time[i]-1, 0)] + cost[i]);
        return dp[n];
    }
};
```
