# Solution - 20 Dec 2023

---
## [2706. Buy Two Chocolates](https://leetcode.com/problems/buy-two-chocolates)

### cpp
```cpp
class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int min1=INT_MAX, min2=INT_MAX;

        for(int i=0; i<prices.size(); i++) {
            int price = prices[i];
            if(price < min1)
                min2 = min1, min1 = price;
            else if(price < min2)
                min2 = price;
        }

        return min1+min2 <= money ? money-min1-min2 : money;
    }
};
```
