# Solution - 24 Mar 2025

---
## [3169. Count Days Without Meetings](https://leetcode.com/problems/count-days-without-meetings)

### cpp
```cpp
class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());
        meetings.push_back({INT_MAX, INT_MAX});

        int sum = 0, start = 0, end = -1;

        for(int i=0; i<meetings.size(); ++i) {
            if(meetings[i][0] <= end)
                end = max(end, meetings[i][1]);
            else {
                sum += end-start+1;
                start = meetings[i][0];
                end = meetings[i][1];
            }
        }

        return days-sum;
    }
};
```
