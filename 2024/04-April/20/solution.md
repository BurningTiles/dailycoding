# Solution - 20 Apr 2024

---
## [1992. Find All Groups of Farmland](https://leetcode.com/problems/find-all-groups-of-farmland)

### cpp
```cpp
class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        vector<vector<int>> ans;
        int n = land.size(), m = land[0].size(), r2, c2;

        for(int r1=0; r1<n; ++r1)
            for(int c1=0; c1<m; ++c1) {
                if(!land[r1][c1]) continue;
                
                for(int i=r1; i<n && land[i][c1]; ++i)
                    for(int j=c1; j<m && land[i][j]; ++j)
                        land[i][j] = 0, r2 = i, c2 = j;
                
                ans.push_back({r1, c1, r2, c2});
            }

        return ans;
    }
};
```
