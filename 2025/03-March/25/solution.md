# Solution - 25 Mar 2025

---
## [3394. Check if Grid can be Cut into Sections](https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections)

### cpp
```cpp
class Solution {
public:
    bool check(vector<vector<int>> &intervals) {
        sort(intervals.begin(), intervals.end());

        int sections = 0, maxEnd = intervals[0][1];

        for(auto &i:intervals) {
            if(maxEnd <= i[0]) ++sections;
            maxEnd = max(maxEnd, i[1]);
        }

        return sections >= 2;
    }

    bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
        vector<vector<int>> xIntervals, yIntervals;

        for(auto &rect:rectangles) {
            xIntervals.push_back({rect[0], rect[2]});
            yIntervals.push_back({rect[1], rect[3]});
        }

        return check(xIntervals) || check(yIntervals);
    }
};
```
