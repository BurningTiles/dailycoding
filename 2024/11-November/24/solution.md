# Solution - 24 Nov 2024

---
## [1975. Maximum Matrix Sum](https://leetcode.com/problems/maximum-matrix-sum)

### cpp
```cpp
class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        long long ans = 0, minVal = INT_MAX, cnt = 0;

        for(int i=0; i<matrix.size(); ++i)
            for(int j=0; j<matrix[i].size(); ++j) {
                ans += abs(matrix[i][j]);
                if(matrix[i][j]<0) ++cnt;
                minVal = min(minVal, (long long)(abs(matrix[i][j])));
            }
        
        return cnt&1 ? ans - minVal * 2 : ans;
    }
};
```
