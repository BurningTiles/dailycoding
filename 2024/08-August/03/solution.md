# Solution - 03 Aug 2024

---
## [1460. Make Two Arrays Equal by Reversing Subarrays](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays)

### cpp
```cpp
class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        unordered_map<int, int> umap;
        
        for(int i=0; i<target.size(); ++i)
            umap[target[i]]++;
        
        for(int i=0; i<arr.size(); ++i)
            if(!umap[arr[i]]--)
                return false;

        return true;
    }
};
```
