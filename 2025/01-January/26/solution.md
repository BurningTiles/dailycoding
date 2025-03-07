# Solution - 26 Jan 2025

---
## [2127. Maximum Employees to Be Invited to a Meeting](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting)

### cpp
```cpp
class Solution {
public:
    int maximumInvitations(vector<int>& favorite) {
        int n = favorite.size();
        vector<int> inDegree(n, 0), chainLengths(n, 0);
        vector<bool> visited(n, false);

        for(int fav:favorite)
            inDegree[fav]++;
        
        queue<int> q;
        for(int i=0; i<n; ++i)
            if(!inDegree[i])
                q.push(i);
        
        while(q.size()) {
            int node = q.front(); q.pop();
            visited[node] = true;

            int next = favorite[node];
            chainLengths[next] = chainLengths[node] + 1;
            if(--inDegree[next] == 0)
                q.push(next);
        }

        int maxCycle = 0, totalChains = 0;
        for(int i=0; i<n; ++i) {
            if(!visited[i]) {
                int curr = i, cycleLength = 0;
                
                while(!visited[curr]) {
                    visited[curr] = true;
                    curr = favorite[curr];
                    cycleLength++;
                }

                if(cycleLength == 2)
                    totalChains += 2 + chainLengths[i] + chainLengths[favorite[i]];
                else
                    maxCycle = max(maxCycle, cycleLength);
            }
        }
        return max(maxCycle, totalChains);
    }
};
```
