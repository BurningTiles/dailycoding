# Solution - 27 Dec 2023

---
## [1578. Minimum Time to Make Rope Colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful)

### cpp
```cpp
auto init = [](){ios::sync_with_stdio(0); cin.tie(0); cout.tie(0); return 0;}();

class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int ans = 0;

        for(int i=1; i<colors.size(); ++i) {
            if(colors[i]==colors[i-1])
                ans += min(neededTime[i], neededTime[i-1]),
                neededTime[i] = max(neededTime[i], neededTime[i-1]);
        }

        return ans;
    }
};
```
