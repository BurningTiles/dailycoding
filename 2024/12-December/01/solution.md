# Solution - 01 Dec 2024

---
## [1346. Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist)

### cpp
```cpp
class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_map<int, int> umap;

        for(int i=0; i<arr.size(); ++i) {
            if(umap[arr[i] * 2] || (arr[i]%2 == 0 && umap[arr[i]/2]))
                return true;
            umap[arr[i]]++;
        }

        return false;
    }
};
```
