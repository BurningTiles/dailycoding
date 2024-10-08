# Solution - 02 Oct 2024

---
## [1331. Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array)

### cpp
```cpp
class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        if(!arr.size()) return {};
        
        vector<pair<int, int>> v(arr.size());
        vector<int> ans(arr.size());

        for(int i=0; i<arr.size(); ++i)
            v[i] = {arr[i], i};
        
        sort(v.begin(), v.end());

        int rank=1;
        ans[v[0].second] = 1; 

        for(int i=1; i<v.size(); ++i) {
            if(v[i].first != v[i-1].first)
                ++rank;
            ans[v[i].second] = rank;
        }

        return ans;
    }
};
```
