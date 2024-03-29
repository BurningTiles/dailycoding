# Solution - 11 Oct 2023

---
## [2251. Number of Flowers in Full Bloom](https://leetcode.com/problems/number-of-flowers-in-full-bloom)

### cpp
```cpp
class Solution {
public:
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& people) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        int n = flowers.size(), m = people.size();
        vector<int> start(n), end(n), ans(m);
        for(int i=0; i<n; ++i)
            start[i] = flowers[i][0], end[i] = flowers[i][1];
        sort(start.begin(), start.end());
        sort(end.begin(), end.end());
        for(int i=0; i<m; ++i) {
            int x = upper_bound(start.begin(), start.end(), people[i]) - start.begin();
            int y = lower_bound(end.begin(), end.end(), people[i]) - end.begin();
            ans[i] = x - y;
        }
        return ans;
    }
};
```
