# Solution - 11 Aug 2024

---
## [1568. Minimum Number of Days to Disconnect Island](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island)

### cpp
```cpp
class Solution {
public:
    bool isValid(int i, int j, int n, int m) {
        return i>=0 && j>=0 && i<n && j<m;
    }

    void dfs(vector<vector<int>> &grid, vector<vector<bool>> &visited, int i, int j) {
        visited[i][j] = true;
        const int cords[] = {0, 1, 0, -1, 0}, n = grid.size(), m = grid[0].size();
        for(int k=0; k<4; ++k) {
            int ii = i+cords[k], jj = j+cords[k+1];
            if(isValid(ii, jj, n, m) && grid[ii][jj] == 1 && !visited[ii][jj])
                dfs(grid, visited, ii, jj);
        }
    }

    int getIslands(vector<vector<int>> &grid) {
        int n = grid.size(), m = grid[0].size(), ans = 0;
        vector<vector<bool>> visited(n, vector<bool>(m, false));

        for(int i=0; i<n; ++i) {
            for(int j=0; j<m; ++j) {
                if(grid[i][j]==1 && !visited[i][j])
                    ++ans, dfs(grid, visited, i, j);
            }
        }

        return ans;
    }

    int minDays(vector<vector<int>>& grid) {
        if(getIslands(grid) != 1) return 0;

        for(int i=0; i<grid.size(); ++i) {
            for(int j=0; j<grid[0].size(); ++j) {
                if(grid[i][j] == 1) {
                    grid[i][j] = 0;
                    if(getIslands(grid) != 1) return 1;
                    grid[i][j] = 1;
                }
            }
        }

        return 2;
    }
};
```
