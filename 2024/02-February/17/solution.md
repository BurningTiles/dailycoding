# Solution - 17 Feb 2024

---
## [1642. Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach)

### cpp
```cpp
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int n = heights.size();
        priority_queue<int> pq;
        
        for(int i=1; i<n; i++){
            int diff = heights[i] - heights[i-1];
            
            if(diff > 0) {
                pq.push(-diff);
                if(pq.size() > ladders) {
                    int minDiff = -pq.top(); pq.pop();
                    if(minDiff > bricks) return i-1;
                    bricks -= minDiff;
                }
            }
        }

        return n-1;
    }
};
```
