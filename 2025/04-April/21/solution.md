# Solution - 21 Apr 2025

---
## [2145. Count the Hidden Sequences](https://leetcode.com/problems/count-the-hidden-sequences)

### cpp
```cpp
class Solution {
public:
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
        long long mn = 0, mx = 0, cur = 0;

        for(auto diff:differences) {
            cur += diff;
            mn = min(mn, cur);
            mx = max(mx, cur);
        }

        int ln1 = mx - mn, ln2 = upper - lower;

        if(ln1 <= ln2)
            return ln2 - ln1 + 1;
    
        return 0;
    }
};
```
