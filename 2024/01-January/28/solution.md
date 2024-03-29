# Solution - 28 Jan 2024

---
## [1074. Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target)

### cpp
```cpp
class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size(), ans = 0;

        for(int i=0; i<m; ++i)
            for(int j=1; j<n; ++j)
                matrix[i][j] += matrix[i][j-1];
        
        for(int i=0; i<n; ++i) {
            for(int j=i; j<n; ++j) {
                unordered_map<int, int> um;
                um[0] = 1;
                int sum = 0;

                for(int k=0; k<m; ++k) {
                    sum += matrix[k][j] - (i ? matrix[k][i-1] : 0);
                    ans += um[sum - target];
                    um[sum]++;
                }
            }
        }

        return ans;
    }
};
```
