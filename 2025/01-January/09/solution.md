# Solution - 09 Jan 2025

---
## [2185. Counting Words With a Given Prefix](https://leetcode.com/problems/counting-words-with-a-given-prefix)

### cpp
```cpp
class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int ans = 0, n = pref.size();
        
        for(auto &word:words) {
            if(word.size() < n) continue;
            int i=0;
            while(i<n) {
                if(word[i] != pref[i]) break;
                ++i;
            }
            ans += i==n;
        }

        return ans;
    }
};
```
