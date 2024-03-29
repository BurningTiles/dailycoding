# Solution - 27 Nov 2023

---
## [935. Knight Dialer](https://leetcode.com/problems/knight-dialer)

### cpp
```cpp
#define MOD 1000000007

class Solution {
public:
    int knightDialer(int n) {
        vector<vector<long long>> neighbors = {
            {4, 6}, {6, 8}, {7, 9}, {4, 8}, {0, 3, 9}, {}, 
            {0, 1, 7}, {2, 6}, {1, 3}, {2, 4}
        };
        vector<long long> counts(10, 1);

        for(int i=1; i<n; i++) {
            vector<long long> next(10, 0);
            for(int j=0; j<10; j++)
                for(auto k:neighbors[j])
                    next[k] += counts[j],
                    next[k] %= MOD;
            counts = next;
        }

        long long ans = 0;
        for(int i=0; i<10; i++)
            ans += counts[i];

        return ans % MOD;
    }
};
```
