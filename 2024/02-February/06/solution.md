# Solution - 06 Feb 2024

---
## [49. Group Anagrams](https://leetcode.com/problems/group-anagrams)

### cpp
```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        unordered_map<string, vector<string>> umap;
        
        for(const auto &str:strs) {
            string key {str};
            ranges::sort(key);
            umap[key].push_back(str);
        }

        for(const auto &[key, val]:umap)
            ans.push_back(val);

        return ans;
    }
};
```
