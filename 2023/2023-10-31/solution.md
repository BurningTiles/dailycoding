# Solution - 31 Oct 2023

---
## [2433. Find The Original Array of Prefix Xor](https://leetcode.com/problems/find-the-original-array-of-prefix-xor)

### cpp
```cpp
class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int prev = pref[0];
        for(int i=1; i<pref.size(); ++i)
            pref[i] ^= prev,
            prev ^= pref[i];
        return pref;
    }
};
```
