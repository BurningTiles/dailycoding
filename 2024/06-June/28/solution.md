# Solution - 28 Jun 2024

---
## [2285. Maximum Total Importance of Roads](https://leetcode.com/problems/maximum-total-importance-of-roads)

### cpp
```cpp
class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        vector<long long> v(n);
        
        for(auto &road:roads)
            ++v[road[0]], ++v[road[1]];

        sort(v.begin(), v.end());
        long long ans = 0;

        for(int i=0; i<v.size(); ++i)
            ans += v[i] * (i+1);
        
        return ans;
    }
};
```
