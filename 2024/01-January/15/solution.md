# Solution - 15 Jan 2024

---
## [2225. Find Players With Zero or One Losses](https://leetcode.com/problems/find-players-with-zero-or-one-losses)

### cpp
```cpp
class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_map<int, pair<int, int>> um;
        vector<vector<int>> ans(2);

        for(auto &match: matches) {
            um[match[0]].first++;
            um[match[1]].second++;
        }

        for(auto [player, rec]: um)
            if(rec.second < 2)
                ans[rec.second].push_back(player);

        sort(ans[0].begin(), ans[0].end());
        sort(ans[1].begin(), ans[1].end());

        return ans;
    }
};
```
