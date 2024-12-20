# Solution - 18 Dec 2024

---
## [1475. Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop)

### cpp
```cpp
class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        stack<int> stk;
        vector<int> ans = prices;

        stk.push(0);
        for(int i=prices.size()-1; i>=0; --i) {
            while(stk.size() && stk.top()>prices[i])
                stk.pop();
            
            if(stk.size())
                ans[i] -= stk.top();
            
            stk.push(prices[i]);
        }

        return ans;
    }
};
```
