# Solution - 05 Aug 2024

---
## [2053. Kth Distinct String in an Array](https://leetcode.com/problems/kth-distinct-string-in-an-array)

### cpp
```cpp
class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        unordered_map<string, int> umap;
        
        for(auto &str:arr)
            umap[str]++;

        for(auto &str:arr)
            if(umap[str] == 1 && !(--k))
                return str;
        
        return "";
    }
};
```
