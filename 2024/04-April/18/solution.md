# Solution - 18 Apr 2024

---
## [463. Island Perimeter](https://leetcode.com/problems/island-perimeter)

### cpp
```cpp
class Solution {
public:
    int isEnd(vector<vector<int>> &grid, int i, int j) {
        if(i<0 || j<0 || i>=grid.size() || j>=grid[0].size())
            return true;
        return grid[i][j]==0;
    }

    int islandPerimeter(vector<vector<int>>& grid) {
        int ans = 0;

        for(int i=0; i<grid.size(); ++i)
            for(int j=0; j<grid[i].size(); ++j)
                if(grid[i][j])
                    ans += isEnd(grid, i-1, j) + isEnd(grid, i+1, j)
                        + isEnd(grid, i, j-1) + isEnd(grid, i, j+1);

        return ans;
    }
};
```
