# Solution - 01 Aug 2024

---
## [2678. Number of Senior Citizens](https://leetcode.com/problems/number-of-senior-citizens)

### cpp
```cpp
class Solution {
public:
    int countSeniors(vector<string>& details) {
        int ans = 0;

        for(auto &detail:details) {
            if(detail[11]>'6' || (detail[11]=='6' && detail[12]>'0'))
                ++ans;
        }

        return ans;
    }
};
```
