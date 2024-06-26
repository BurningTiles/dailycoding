# Solution - 18 Jun 2024

---
## [826. Most Profit Assigning Work](https://leetcode.com/problems/most-profit-assigning-work)

### cpp
```cpp
class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        vector<pair<int, int>> dp; // Difficulty profit array
        int n=profit.size(), ans = 0, i = 0, maxProfit = 0;

        for(int j=0; j<n; ++j)
            dp.push_back({difficulty[j], profit[j]});

        sort(dp.begin(), dp.end());
        sort(worker.begin(), worker.end());

        for(int ability:worker) {
            while(i < n && ability >= dp[i].first)
                maxProfit = max(dp[i++].second, maxProfit);
            ans += maxProfit;
        }

        return ans;
    }
};
```
