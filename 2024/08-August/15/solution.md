# Solution - 15 Aug 2024

---
## [860. Lemonade Change](https://leetcode.com/problems/lemonade-change)

### cpp
```cpp
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int cash[] = {0, 0, 0, 0, 0};

        for(int i=0; i<bills.size(); ++i) {
            int give = bills[i] - 5;

            if(give >= 10 && cash[2]) 
                --cash[2], give -= 10;
            while(give >= 5 && cash[1])
                --cash[1], give -= 5;

            if(give != 0) return false;

            cash[bills[i]/5]++;
        }

        return true;
    }
};
```
