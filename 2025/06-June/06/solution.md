# Solution - 06 Jun 2025

---
## [2434. Using a Robot to Print the Lexicographically Smallest String](https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string)

### cpp
```cpp
class Solution {
public:
    string robotWithString(string s) {
        string p, t;
        int cnt[26] = {}, i=0;

        for(auto ch:s) ++cnt[ch-'a'];
    
        for(auto ch:s) {
            t.push_back(ch);
            --cnt[ch-'a'];

            while(i < 25 && cnt[i] == 0)
                ++i;
            while(t.size() && t.back() - 'a' <= i) {
                p.push_back(t.back());
                t.pop_back();
            }
        }

        return p;
    }
};
```
