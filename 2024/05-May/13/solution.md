# Solution - 13 May 2024

---
## [861. Score After Flipping Matrix](https://leetcode.com/problems/score-after-flipping-matrix)

### cpp
```cpp
class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
        int n=grid.size(), m=grid[0].size(), ans = n * (1 << (m-1));

        for(int j=1; j<m; ++j) {
            int cnt = 0;
            for(int i=0; i<n; ++i)
                cnt += grid[i][j] == grid[i][0];
            ans += max(cnt, n-cnt) * (1 << (m-j-1));
        }

        return ans;
    }
};
```
