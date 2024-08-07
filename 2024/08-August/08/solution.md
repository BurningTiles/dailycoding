# Solution - 08 Aug 2024

---
## [885. Spiral Matrix III](https://leetcode.com/problems/spiral-matrix-iii)

### cpp
```cpp
class Solution {
public:
    bool isValid(int m, int n, int i, int j) {
        return i>=0 && i<m && j>=0 && j<n;
    }

    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        int l=cStart, r=cStart, t=rStart, b=rStart;
        vector<vector<int>> ans;

        while(l>=0 || r<cols || t>=0 || b<rows) {
            for(int i=l; i<=r; ++i)
                if(isValid(rows, cols, t, i))
                    ans.push_back({t, i});
            r += 1;

            for(int i=t; i<=b; ++i)
                if(isValid(rows, cols, i, r))
                    ans.push_back({i, r});
            b += 1;
            
            for(int i=r; i>=l; --i)
                if(isValid(rows, cols, b, i))
                    ans.push_back({b, i});
            l -= 1;
            
            for(int i=b; i>=t; --i)
                if(isValid(rows, cols, i, l))
                    ans.push_back({i, l});
            t -= 1;
        }

        return ans;
    }
};
```
