# Solution - 17 Feb 2025

---
## [1079. Letter Tile Possibilities](https://leetcode.com/problems/letter-tile-possibilities)

### cpp
```cpp
class Solution {
public:
    void helper(int cnt[26], int &ans) {
        for(int i=0; i<26; ++i) {
            if(cnt[i]) {
                --cnt[i];
                ++ans;
                helper(cnt, ans);
                ++cnt[i];
            }
        }
    }

    int numTilePossibilities(string tiles) {
        int cnt[26] = {0}, ans = 0;
        
        for(auto ch:tiles)
            cnt[ch-'A']++;
        
        helper(cnt, ans);
        return ans;
    }
};
```
