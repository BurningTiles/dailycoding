# Solution - 09 Jul 2025

---
## [3439. Reschedule Meetings for Maximum Free Time I](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i)

### cpp
```cpp
class Solution {
public:
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        const int n = startTime.size();
        int busy = 0;

        for(int i=0; i<k; ++i)
            busy += endTime[i] - startTime[i];
        
        if(n==k) return eventTime-busy;

        int ans = startTime[k]-busy;

        for(int l=0, r=k; r<n; l++, r++) {
            busy += (endTime[r]-startTime[r]) - (endTime[l]-startTime[l]);
            int end = (r==n-1) ? eventTime : startTime[r+1];
            int start = endTime[l];
            ans = max(ans, end-start-busy);
        }

        return ans;
    }
};
```
