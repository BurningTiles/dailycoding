# Solution - 27 Dec 2024

---
## [1014. Best Sightseeing Pair](https://leetcode.com/problems/best-sightseeing-pair)

### cpp
```cpp
class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int ans = INT_MIN, mx = values[0], mxi = 0;

        for(int i=1; i<values.size(); ++i) {
            int tmp = mx + mxi - i;
            ans = max(ans, tmp + values[i]);

            if(values[i] > tmp)
                mx = values[i], mxi = i;
        }

        return ans;
    }
};
```
