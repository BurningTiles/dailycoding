# Solution - 11 May 2024

---
## [857. Minimum Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers)

### cpp
```cpp
class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        vector<pair<double, int>> v;
        double ans = DBL_MAX, qualitySum = 0;

        for (int i = 0; i < wage.size(); ++i)
            v.push_back({double(wage[i]) / quality[i], quality[i]});

        sort(v.begin(), v.end());

        priority_queue<int> pq;
        for (auto p : v) {
            qualitySum += p.second, pq.push(p.second);
            if (pq.size() > k)
                qualitySum -= pq.top(), pq.pop();
            if (pq.size() == k)
                ans = min(ans, qualitySum * p.first);
        }

        return ans;
    }
};
```
