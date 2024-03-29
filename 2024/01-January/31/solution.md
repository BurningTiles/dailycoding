# Solution - 31 Jan 2024

---
## [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures)

### cpp
```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> stk;
        vector<int> ans(temperatures.size());

        for(int i=temperatures.size()-1; i>=0; --i) {
            int temp = temperatures[i];

            while(stk.size() && stk.top().first <= temp)
                stk.pop();
            
            ans[i] = stk.size() ? (stk.top().second - i) : 0;
            stk.push({temp, i});
        }

        return ans;
    }
};
```
