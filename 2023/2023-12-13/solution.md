# Solution - 13 Dec 2023

---
## [1582. Special Positions in a Binary Matrix](https://leetcode.com/problems/special-positions-in-a-binary-matrix)

### cpp
```cpp
class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        vector<int> col(mat[0].size(), 0);
        int ans = 0;
        
        for(int i=0; i<mat.size(); i++) {
            int jx = -1;
            for(int j=0; j<mat[i].size(); j++)
                if(mat[i][j]) {
                    if(jx != -1) {
                        jx = -1; break;
                    } else jx = j;
                }

            if(jx != -1 && col[jx] == 0) {
                int ix = 0;
                for(; ix<mat.size(); ix++)
                    if(mat[ix][jx] && ix!=i) break;
                if(ix==mat.size()) ++ans;
                else col[jx] = 1;
            }
        }

        return ans;
    }
};
```
