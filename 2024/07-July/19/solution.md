# Solution - 19 Jul 2024

---
## [1380. Lucky Numbers in a Matrix](https://leetcode.com/problems/lucky-numbers-in-a-matrix)

### cpp
```cpp
class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<int> ans, col(m, INT_MAX), row(n);

        for(int i=0; i<m; ++i)
            for(int j=0; j<n; ++j)
                col[i] = min(col[i], matrix[i][j]),
                row[j] = max(row[j], matrix[i][j]);

        for(int i=0; i<m; ++i)
            for(int j=0; j<n; ++j)
                if(matrix[i][j] == col[i] && matrix[i][j] == row[j])
                    ans.push_back(matrix[i][j]);
        
        return ans;
    }
};
```
