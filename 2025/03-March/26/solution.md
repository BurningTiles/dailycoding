# Solution - 26 Mar 2025

---
## [2033. Minimum Operations to Make a Uni-Value Grid](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid)

### cpp
```cpp
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        vector<int> arr;
        for(int i=0; i<grid.size(); ++i)
            arr.insert(arr.end(), grid[i].begin(), grid[i].end());

        sort(arr.begin(), arr.end());

        int median = arr[arr.size() / 2], ans = 0;

        for(int i=arr.size()-1; i>=0; --i) {
            if(abs(arr[i] - median) % x) return -1;
            ans += abs(arr[i] - median) / x;
        }

        return ans;
    }
};
```
