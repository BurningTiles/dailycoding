# Solution - 09 Apr 2024

---
## [2073. Time Needed to Buy Tickets](https://leetcode.com/problems/time-needed-to-buy-tickets)

### cpp
```cpp
class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int ans = 0;

        for(int i=0; i<tickets.size(); ++i)
            ans += min(tickets[i], tickets[k]-(i>k));

        return ans;
    }
};
```
