# Solution - 12 May 2024

---
## [2373. Largest Local Values in a Matrix](https://leetcode.com/problems/largest-local-values-in-a-matrix)

### cpp
```cpp
class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n=grid.size(), m=grid[0].size();
        vector<vector<int>> ans(n-2, vector<int>(m-2, 0));

        for(int i=0; i<n-2; ++i)
            for(int j=0; j<m-2; ++j)
                for(int x=i; x<i+3; ++x)
                    for(int y=j; y<j+3; ++y)
                        ans[i][j] = max(ans[i][j], grid[x][y]);

        return ans;
    }
};
```
