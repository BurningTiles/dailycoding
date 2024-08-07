# Solution - 09 Aug 2024

---
## [840. Magic Squares In Grid](https://leetcode.com/problems/magic-squares-in-grid)

### cpp
```cpp
class Solution {
public:
    bool isMagicSquare(vector<vector<int>>& grid, int x, int y) {
        if (grid[x + 1][y + 1] != 5)
            return false;

        int used[10] = {0};

        for (int i = x; i < x + 3; ++i)
            for (int j = y; j < y + 3; ++j)
                if (grid[i][j] == 0 || grid[i][j] > 9)
                    return false;
                else if (used[grid[i][j]])
                    return false;
                else
                    used[grid[i][j]]++;

        if ((grid[x][y] + grid[x][y + 1] + grid[x][y + 2]) != 15)
            return false;
        if ((grid[x][y] + grid[x + 1][y + 1] + grid[x + 2][y + 2]) != 15)
            return false;
        if ((grid[x][y] + grid[x + 1][y] + grid[x + 2][y]) != 15)
            return false;
        if ((grid[x + 2][y] + grid[x + 2][y + 1] + grid[x + 2][y + 2]) != 15)
            return false;
        if ((grid[x][y + 2] + grid[x + 1][y + 2] + grid[x + 2][y + 2]) != 15)
            return false;
        if ((grid[x][y + 2] + grid[x + 1][y + 1] + grid[x + 2][y]) != 15)
            return false;
        return true;
    }

    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size(), ans = 0;

        for (int i = 0; i < n - 2; ++i)
            for (int j = 0; j < m - 2; ++j)
                if (isMagicSquare(grid, i, j))
                    ++ans;

        return ans;
    }
};
```
