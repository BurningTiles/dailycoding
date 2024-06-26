# Solution - 14 May 2024

---
## [1219. Path with Maximum Gold](https://leetcode.com/problems/path-with-maximum-gold)

### cpp
```cpp
class Solution {
public:
    int getMaximumGold(vector<vector<int>>& grid) {
        int ans = 0;

        for (int i = 0; i < grid.size(); ++i)
            for (int j = 0; j < grid[i].size(); ++j)
                if (grid[i][j])
                    dfs(grid, ans, 0, i, j);

        return ans;
    }

    void dfs(vector<vector<int>>& grid, int& ans, int cur, int i, int j, int depth = 0) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() ||
            !grid[i][j] || depth >= 25)
            return;

        int val = grid[i][j];
        cur += val;
        ans = max(ans, cur);

        grid[i][j] = 0;
        dfs(grid, ans, cur, i+1, j, depth+1);
        dfs(grid, ans, cur, i-1, j, depth+1);
        dfs(grid, ans, cur, i, j+1, depth+1);
        dfs(grid, ans, cur, i, j-1, depth+1);
        grid[i][j] = val;
    }
};
```
