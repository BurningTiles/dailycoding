# Solution - 27 Oct 2024

---
## [1277. Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones)

### cpp
```cpp
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int ans = 0;

        for(int i=0; i<matrix.size(); ++i) {
            for(int j=0; j<matrix[i].size(); ++j) {
                if(i>0 && j>0 && matrix[i][j]>0)
                    matrix[i][j] = 1 + min(matrix[i-1][j-1], min(matrix[i-1][j], matrix[i][j-1]));
                
                ans += matrix[i][j];
            }
        }

        return ans;
    }
};
```
