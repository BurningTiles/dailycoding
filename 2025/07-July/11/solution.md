# Solution - 11 Jul 2025

---
## [2402. Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii)

### cpp
```cpp
#define ll long long
#define pli pair<ll, int>

class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());
        priority_queue<pli, vector<pli>, greater<pli>> pq;
        priority_queue<int, vector<int>, greater<int>> free;
        vector<int> count(n, 0);

        for(int i=0; i<n; ++i) free.push(i);

        for(auto &m:meetings) {
            ll start = m[0], end = m[1];

            while(pq.size() > 0 && pq.top().first <= start) {
                int room = pq.top().second; pq.pop();
                free.push(room);
            }

            if(free.size() > 0) {
                int room = free.top(); free.pop();
                ++count[room];
                pq.push({end, room});
            }
            else {
                pli tmp = pq.top(); pq.pop();
                ++count[tmp.second];

                end = tmp.first + (end - start);
                pq.push({end, tmp.second});
            }
        }
        
        return max_element(count.begin(), count.end()) - count.begin();
    }
};
```
