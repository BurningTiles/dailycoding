# Solution - 16 Oct 2023

---
## [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii)

### cpp
```cpp
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> ans(rowIndex+1);
        ans.front() = 1;
        long long tmp = 1;
        for(int i=1; i<=rowIndex; i++) {
            tmp = tmp * (rowIndex - i + 1);
            tmp = tmp / i;
            ans[i] = tmp;
        }
        return ans;
    }
};
```
