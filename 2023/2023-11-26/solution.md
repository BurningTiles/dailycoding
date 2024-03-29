# Solution - 26 Nov 2023

---
## [1727. Largest Submatrix With Rearrangements](https://leetcode.com/problems/largest-submatrix-with-rearrangements)

### cpp
```cpp
class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        int ans = count(matrix[0].begin(), matrix[0].end(), 1);

        for(int i=1; i<m; ++i)
            for(int j=0; j<n; ++j)
                if(matrix[i][j])
                    matrix[i][j] += matrix[i-1][j];

        for(int i=1; i<m; ++i) {
            sort(matrix[i].begin(), matrix[i].end());
            for(int j=0; j<n; ++j) 
                ans = max(ans, matrix[i][j]*(n-j));
        }
        
        return ans;
    }
};
```
