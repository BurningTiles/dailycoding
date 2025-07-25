# Solution - 23 Jul 2025

---
## [1717. Maximum Score From Removing Substrings](https://leetcode.com/problems/maximum-score-from-removing-substrings)

### cpp
```cpp
class Solution {
public:
    int maximumGain(string s, int x, int y) {
        int aCnt = 0, bCnt = 0, low = min(x, y), ans = 0;

        for(char c:s) {
            if(c > 'b') {
                ans += min(aCnt, bCnt) * low;
                aCnt = bCnt = 0;
            } else if(c == 'a') {
                if(x < y && bCnt > 0)
                    --bCnt, ans += y;
                else
                    ++aCnt;
            } else {
                if(x > y && aCnt > 0)
                    --aCnt, ans += x;
                else
                    ++bCnt;
            }
        }

        ans += min(aCnt, bCnt) * low;
        return ans;
    }
};
```
