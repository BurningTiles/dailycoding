# Solution - 01 Sep 2024

---
## [2022. Convert 1D Array Into 2D Array](https://leetcode.com/problems/convert-1d-array-into-2d-array)

### cpp
```cpp
class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        if(m*n != original.size()) return {};
        
        vector<vector<int>> ans(m, vector<int>(n));

        for(int i=0; i<m; ++i)
            for(int j=0; j<n; ++j)
                ans[i][j] = original[i*n + j];

        return ans;
    }
};
```
