# Solution - 28 Aug 2024

---
## [1905. Count Sub Islands](https://leetcode.com/problems/count-sub-islands)

### cpp
```cpp
class Solution {
public:
    bool isSubIsland(vector<vector<int>> &grid1, vector<vector<int>> &grid2, vector<vector<bool>> &visited, int i, int j) {
        if(i<0 || j<0 || i>=grid1.size() || j>=grid1[0].size() || visited[i][j])
            return true;

        visited[i][j] = true;

        if(grid2[i][j] == 0)
            return true;

        bool ans = (grid2[i][j] == grid1[i][j]) &
            isSubIsland(grid1, grid2, visited, i+1, j) &
            isSubIsland(grid1, grid2, visited, i-1, j) &
            isSubIsland(grid1, grid2, visited, i, j+1) &
            isSubIsland(grid1, grid2, visited, i, j-1);
        
        return ans;
    }

    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int ans = 0, m = grid1.size(), n = grid1[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));

        for(int i=0; i<m; ++i)
            for(int j=0; j<n; ++j)
                if(grid2[i][j] && !visited[i][j] && isSubIsland(grid1, grid2, visited, i, j))
                    ++ans;

        return ans;
    }
};
```
