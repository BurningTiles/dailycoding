# Solution - 15 Dec 2024

---
## [1792. Maximum Average Pass Ratio](https://leetcode.com/problems/maximum-average-pass-ratio)

### cpp
```cpp
class Solution {
public:
    double profit(double pass, double total) {
        return (pass+1) / (total+1) - pass / total;
    }

    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        double totalPassRatio = 0;
        priority_queue<pair<double, array<int, 2>>> pq;

        for(auto &c:classes) {
            totalPassRatio += (double) c[0] / c[1];
            pq.push({profit(c[0], c[1]), {c[0], c[1]}});
        }

        while(extraStudents--) {
            auto [extraProfit, _class] = pq.top(); pq.pop();
            totalPassRatio += extraProfit;
            _class[0]++, _class[1]++;
            pq.push({ profit(_class[0], _class[1]), {_class[0], _class[1]}});
        }

        return totalPassRatio / classes.size();
    }
};
```
