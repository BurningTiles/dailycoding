# Solution - 30 Dec 2023

---
## [1897. Redistribute Characters to Make All Strings Equal](https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal)

### cpp
```cpp
class Solution {
public:
    bool makeEqual(vector<string>& words) {
        int cnt[128] = {0}, n = words.size();

        for(int i=0; i<n; ++i)
            for(auto ch: words[i])
                cnt[ch]++;
        
        for(int i=97; i<124; ++i)
            if(cnt[i] % n) return false;

        return true;
    }
};
```
