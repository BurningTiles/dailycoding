# Solution - 07 Jul 2024

---
## [1518. Water Bottles](https://leetcode.com/problems/water-bottles)

### cpp
```cpp
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int full = numBottles, empty = 0, ans = 0;

        while(full || empty >= numExchange) {
            if(full) ans += full, empty += full, full = 0;
            else full = empty / numExchange, empty %= numExchange;
        }

        return ans;
    }
};
```
