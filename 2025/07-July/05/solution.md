# Solution - 05 Jul 2025

---
## [1394. Find Lucky Integer in an Array](https://leetcode.com/problems/find-lucky-integer-in-an-array)

### cpp
```cpp
class Solution {
public:
    int findLucky(vector<int>& arr) {
        int cnt[501] = {0};

        for(auto n:arr) cnt[n]++;

        for(int i=500; i>0; --i)
            if(cnt[i] == i) return i;
        
        return -1;
    }
};
```
