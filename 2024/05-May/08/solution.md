# Solution - 08 May 2024

---
## [506. Relative Ranks](https://leetcode.com/problems/relative-ranks)

### cpp
```cpp
class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        unordered_map<int, int> um;
        vector<string> ans(score.size()), rank = {"Gold Medal", "Silver Medal", "Bronze Medal"};
        
        for(int i=0; i<score.size(); ++i)
            um[score[i]] = i;
        
        sort(score.rbegin(), score.rend());

        for(int i=0; i<score.size(); ++i) {
            if(i<3) ans[um[score[i]]] = rank[i];
            else ans[um[score[i]]] = to_string(i+1);
        }

        return ans;
    }
};
```
