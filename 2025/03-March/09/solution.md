# Solution - 09 Mar 2025

---
## [3208. Alternating Groups II](https://leetcode.com/problems/alternating-groups-ii)

### cpp
```cpp
class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        // int n = colors.size();
        colors.insert(colors.end(), colors.begin(), colors.begin() + k);

        int last = 0, ans = 0, i=1;
        for(; i<colors.size(); ++i) {
            if(colors[i] == colors[i-1]) {
                ans += max(0, i-last-k+1);
                last = i;
            }
        }
        ans += max(0, i-last-k);

        return ans;
    }
};
```
