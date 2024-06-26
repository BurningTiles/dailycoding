# Solution - 26 Apr 2024

---
## [1289. Minimum Falling Path Sum II](https://leetcode.com/problems/minimum-falling-path-sum-ii)

### cpp
```cpp
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        int m = grid[0].size(), ans = INT_MAX;

        for (int i = 1; i < grid.size(); ++i) {
            int mn1 = -1, mn2 = -1;
            for (int j=0; j<m; ++j) {
                if(mn1==-1 || grid[i-1][j] < grid[i-1][mn1]) mn2 = mn1, mn1 = j;
                else if(mn2==-1 || grid[i-1][j] < grid[i-1][mn2]) mn2 = j;
            }

            for (int j = 0; j < m; ++j) {
                int ans = INT_MAX;
                if(mn1 == j) grid[i][j] += grid[i-1][mn2];
                else grid[i][j] += grid[i-1][mn1];
            }
        }

        for(int x:grid.back())
            ans = min(ans, x);

        return ans;
    }
};
```
