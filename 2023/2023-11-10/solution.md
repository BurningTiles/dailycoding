# Solution - 10 Nov 2023

---
## [1743. Restore the Array From Adjacent Pairs](https://leetcode.com/problems/restore-the-array-from-adjacent-pairs)

### cpp
```cpp
class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        unordered_map<int, vector<int>> um;
        for(auto &pair:adjacentPairs) {
            um[pair[0]].push_back(pair[1]);
            um[pair[1]].push_back(pair[0]);
        }
        
        vector<int> ans;
        for(auto [key, val]:um) {
            if(val.size()==1){
                ans = {key, val[0]};
                break;
            }
        }

        for(int i=2; i<um.size(); i++) {
            vector<int> &x = um[ans[i-1]];
            ans.push_back(x[0]==ans[i-2] ? x[1] : x[0]);
        }

        return ans;
    }
};
```
