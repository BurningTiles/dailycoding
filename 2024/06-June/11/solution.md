# Solution - 11 Jun 2024

---
## [1122. Relative Sort Array](https://leetcode.com/problems/relative-sort-array)

### cpp
```cpp
class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> um;
        vector<int> ans;
        int len = 0;

        for (int a : arr1)
            um[a]++;

        for (int a : arr2)
            while (um[a]) {
                um[a]--, ++len;
                ans.push_back(a);
                if (!um[a])
                    um.erase(a);
            }

        for (auto p : um)
            while (p.second)
                ans.push_back(p.first), --p.second;

        sort(ans.begin() + len, ans.end());
        return ans;
    }
};
```
