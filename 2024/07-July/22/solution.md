# Solution - 22 Jul 2024

---
## [2418. Sort the People](https://leetcode.com/problems/sort-the-people)

### cpp
```cpp
class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<pair<int, string>> tmp;

        for(int i=0; i<names.size(); ++i)
            tmp.push_back({heights[i], names[i]});
        
        sort(tmp.rbegin(), tmp.rend());

        vector<string> ans;

        for(auto &t:tmp)
            ans.push_back(t.second);

        return ans;
    }
};
```
