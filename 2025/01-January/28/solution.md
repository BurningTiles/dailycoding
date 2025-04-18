# Solution - 28 Jan 2025

---
## [2658. Maximum Number of Fish in a Grid](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid)

### cpp
```cpp
class Solution {
public:
    int getFish(vector<vector<int>> &grid, int i, int j) {
        int ans = grid[i][j], p[] = {0,1,0,-1,0}, n=grid.size(), m=grid[0].size();
        grid[i][j] = 0;

        for(int t=0; t<4; ++t) {
            int x=i+p[t], y=j+p[t+1];
            if(x>=0 && x<n && y>=0 && y<m && grid[x][y]>0)
                ans += getFish(grid, x, y);
        }

        return ans;
    }

    int findMaxFish(vector<vector<int>>& grid) {
        int ans = 0, n = grid.size(), m = grid[0].size();

        for(int i=0; i<n; ++i)
            for(int j=0; j<m; ++j)
                if(grid[i][j])
                    ans = max(ans, getFish(grid, i, j));

        return ans;
    }
};
```
