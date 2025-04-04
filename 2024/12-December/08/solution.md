# Solution - 08 Dec 2024

---
## [2054. Two Best Non-Overlapping Events](https://leetcode.com/problems/two-best-non-overlapping-events)

### cpp
```cpp
class Solution {
public:
    int maxTwoEvents(vector<vector<int>>& events) {
        int n = events.size(), ans = 0;
        vector<int> maxFrom(n);

        sort(events.begin(), events.end(), [](vector<int> &a, vector<int> &b) {
            return a[0] < b[0];
        });

        maxFrom[n-1] = events[n-1][2];
        for(int i=n-2; i>=0; --i)
            maxFrom[i] = max(events[i][2], maxFrom[i+1]);
        
        for(int i=0; i<n; ++i) {
            int l=i+1, r=n-1, nextIndex = -1;

            while(l <= r) {
                int mid = l + (r-l) / 2;
                if(events[mid][0] > events[i][1]) {
                    nextIndex = mid;
                    r = mid - 1;
                } else
                    l = mid + 1;
            }

            if(nextIndex != -1)
                ans = max(ans, events[i][2] + maxFrom[nextIndex]);
            
            ans = max(ans, events[i][2]);
        }

        return ans;
    }
};
```
