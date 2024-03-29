# Solution - 11 Feb 2024

---
## [1463. Cherry Pickup II](https://leetcode.com/problems/cherry-pickup-ii)

### cpp
```cpp
class Solution {
public:
    int dp[70][70][70];

    int cherryPickup(vector<vector<int>>& grid) {
        memset(dp, -1, sizeof(dp)); // Init array with value -1
        int m = grid.size(), n = grid[0].size();
        return helper(grid, m, n, 0, 0, n-1); // Call dfs recursive helper function.
    }

    // m = totalRows, n = totalCols, r = currentRow, p1, p2 = column position of robot1 & robot2
    int helper(vector<vector<int>> &grid, int m, int n, int r, int p1, int p2) {
        if(r == m) return 0; // Reached bottom row.
        if(dp[r][p1][p2] != -1) return dp[r][p1][p2]; // If value already exist then return.

        int ans = 0; // Max cherries collected in next line positions
        for(int i=max(0, p1-1); i<min(p1+2, n); ++i)
            for(int j=max(0, p2-1); j<min(p2+2, n); ++j)
                ans = max(ans, helper(grid, m, n, r+1, i, j));

        return dp[r][p1][p2] = ans + (p1 == p2 ? grid[r][p1] : grid[r][p1] + grid[r][p2]);
    }
};
```
