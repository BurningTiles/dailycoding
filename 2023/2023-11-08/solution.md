# Solution - 08 Nov 2023

---
## [2849. Determine if a Cell Is Reachable at a Given Time](https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time)

### cpp
```cpp
class Solution {
public:
    bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        if(sx==fx && sy==fy) return t > 1 || t == 0;
        return t >= max(abs(sx-fx), abs(sy-fy));
    }
};
```
