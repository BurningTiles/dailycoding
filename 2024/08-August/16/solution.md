# Solution - 16 Aug 2024

---
## [624. Maximum Distance in Arrays](https://leetcode.com/problems/maximum-distance-in-arrays)

### cpp
```cpp
class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int minimum = arrays[0][0], maximum = arrays[0].back(), ans = 0;

        for(int i=1; i<arrays.size(); ++i) {
            ans = max(ans, abs(arrays[i].back() - minimum));
            ans = max(ans, abs(maximum - arrays[i][0]));
            minimum = min(minimum, arrays[i][0]);
            maximum = max(maximum, arrays[i].back());
        }

        return ans;
    }
};
```
