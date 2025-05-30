# Solution - 29 Oct 2024

---
## [2684. Maximum Number of Moves in a Grid](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid)

### cpp
```cpp
class Solution {
public:
    int maxMoves(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size(), ans = 0;

        vector<vector<int>> moves(n, vector<int>(m, 0));
        for(int i=0; i<n; ++i)
            moves[i][0] = 1;

        for(int j=1; j<m; ++j) {
            for(int i=0; i<n; ++i) {
                int steps = (grid[i][j-1] < grid[i][j] && moves[i][j-1] > 0)
                    ? moves[i][j-1] + 1 : 0;
                steps = max(steps, (i>0 && grid[i-1][j-1] < grid[i][j] && moves[i-1][j-1] > 0)
                    ? moves[i-1][j-1] + 1 : 0);
                steps = max(steps, (i<n-1 && grid[i+1][j-1] < grid[i][j] && moves[i+1][j-1] > 0)
                    ? moves[i+1][j-1] + 1 : 0);
                
                moves[i][j] = steps;
                ans = max(ans, steps-1);
            }
        }
        
        return ans;
    }
};
```
