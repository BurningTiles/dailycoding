# Solution - 18 Mar 2024

---
## [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons)

### cpp
```cpp
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        for(auto &p:points) swap(p[0], p[1]);

        sort(points.begin(), points.end());
        int ans = 0, n=points.size();

        for(int i=0; i<n; ++i) {
            int j=i;
            while(j<n && points[j][1] <= points[i][0]) ++j;
            ++ans, i = j-1;
        }

        return ans;
    }
};
```
