# Solution - 15 Jun 2025

---
## [1432. Max Difference You Can Get From Changing an Integer](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer)

### cpp
```cpp
class Solution {
public:
    int maxDiff(int num) {
        string s = to_string(num);
        set<char> unique(s.begin(), s.end());
        int mx = num, mn = num;

        for(char digit:unique) {
            for(char newDigit = '0'; newDigit <= '9'; ++newDigit) {
                if(s[0] == digit && newDigit == '0') continue;
                string tmps = s;
                replace(tmps.begin(), tmps.end(), digit, newDigit);
                int tmpn = stoi(tmps);
                mx = max(mx, tmpn);
                mn = min(mn, tmpn);
            }
        }

        return mx - mn;
    }
};
```
