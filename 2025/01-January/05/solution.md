# Solution - 05 Jan 2025

---
## [2381. Shifting Letters II](https://leetcode.com/problems/shifting-letters-ii)

### cpp
```cpp
class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        vector<int> diff(s.size() + 1, 0);
        
        for(auto &shift:shifts) {
            int change = shift[2] == 0 ? -1 : 1;
            diff[shift[0]] += change;
            diff[shift[1]+1] -= change;
        }

        for(int i=0, c=0, ch=0; i<s.size(); ++i) {
            c += diff[i];
            ch = s[i] + (c%26);
            if(ch < 'a') ch += 26;
            if(ch > 'z') ch -= 26;
            s[i] = ch;
        }

        return s;
    }
};
```
