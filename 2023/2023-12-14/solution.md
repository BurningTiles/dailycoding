# Solution - 14 Dec 2023

---
## [2482. Difference Between Ones and Zeros in Row and Column](https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column)

### cpp
```cpp
class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int m=grid.size(), n=grid[0].size();
        vector<int> row(m, 0), col(n, 0);
        vector<vector<int>> ans(m, vector<int>(n));

        for(int i=0; i<m; i++)
            for(int j=0; j<n; j++)
                if(grid[i][j]) ++row[i], ++col[j];
                else --row[i], --col[j];
        
        for(int i=0; i<m; i++)
            for(int j=0; j<n; j++)
                ans[i][j] = row[i] + col[j];

        return ans;
    }
};
```
