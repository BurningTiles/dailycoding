# Solution - 19 Apr 2024

---
## [200. Number of Islands](https://leetcode.com/problems/number-of-islands)

### cpp
```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size(), m = grid[0].size(), ans = 0;

        for(int i=0; i<n; ++i)
            for(int j=0; j<m; ++j)
                if(grid[i][j]=='1') {
                    ++ans;
                    queue<pair<int, int>> q;
                    q.push({i, j});
                    while(q.size()) {
                        auto [x, y] = q.front(); q.pop();
                        if(x>=0 && y>=0 && x<n && y<m && grid[x][y]=='1') {
                            grid[x][y] = '0';
                            q.push({x+1, y});
                            q.push({x-1, y});
                            q.push({x, y+1});
                            q.push({x, y-1});
                        }
                    }
                }

        return ans;
    }
};
```
