# Solution - 12 Jan 2024

---
## [1704. Determine if String Halves Are Alike](https://leetcode.com/problems/determine-if-string-halves-are-alike)

### cpp
```cpp
class Solution {
public:
    bool halvesAreAlike(string s) {
        int cnt = 0, half = s.size()/2;
        const string vovels = "aeiouAEIOU";
        
        for(int i=0; i<s.size(); ++i)
            if(vovels.find(s[i]) != -1)
                cnt += i>=half ? -1 : 1;
        
        return cnt == 0;
    }
};
```
