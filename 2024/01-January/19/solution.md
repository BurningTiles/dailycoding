# Solution - 19 Jan 2024

---
## [931. Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum)

### cpp
```cpp
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size(), ans = INT_MAX;

        for(int i=0; i<n; ++i) {
            for(int j=0; j<n; ++j) {
                if(i>0) {
                    int val = matrix[i][j];
                    matrix[i][j] = matrix[i-1][j] + val;
                    if(j>0)
                        matrix[i][j] = min(matrix[i][j], matrix[i-1][j-1] + val);
                    if(j<n-1)
                        matrix[i][j] = min(matrix[i][j], matrix[i-1][j+1] + val);
                }
                
                if(i==n-1) ans = min(ans, matrix[i][j]);
            }
        }

        return ans;
    }
};
```
