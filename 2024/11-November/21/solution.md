# Solution - 21 Nov 2024

---
## [2257. Count Unguarded Cells in the Grid](https://leetcode.com/problems/count-unguarded-cells-in-the-grid)

### cpp
```cpp
class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<vector<char>> grid(m, vector<char>(n, 'U'));

        for(auto &g:guards)
            grid[g[0]][g[1]] = 'G';
        
        for(auto &w:walls)
            grid[w[0]][w[1]] = 'W';
        
        for(auto &g:guards) {
            int row=g[0], col=g[1];

            // UP
            for(int i=row-1; i>=0; --i)
                if(grid[i][col]=='G' || grid[i][col]=='W') break;
                else grid[i][col] = 'S';
            
            // Right
            for(int i=col+1; i<n; ++i)
                if(grid[row][i]=='G' || grid[row][i]=='W') break;
                else grid[row][i] = 'S';
            
            // Down
            for(int i=row+1; i<m; ++i)
                if(grid[i][col]=='G' || grid[i][col]=='W') break;
                else grid[i][col] = 'S';
            
            // Left
            for(int i=col-1; i>=0; --i)
                if(grid[row][i]=='G' || grid[row][i]=='W') break;
                else grid[row][i] = 'S';
        }

        int ans = 0;
        for(int i=0; i<m; ++i)
            for(int j=0; j<n; ++j)
                if(grid[i][j]=='U') ++ans;

        return ans;
    }
};
```
