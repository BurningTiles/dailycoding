# Solution - 07 Oct 2024

---
## [2696. Minimum String Length After Removing Substrings](https://leetcode.com/problems/minimum-string-length-after-removing-substrings)

### cpp
```cpp
class Solution {
public:
    int minLength(string s) {
        vector<int> v;
        
        for(int i=0; i<s.size(); ++i) {
            if(s[i] == 'B' && v.size() && v.back() == 'A')
                v.pop_back();
            else if(s[i] == 'D' && v.size() && v.back() == 'C')
                v.pop_back();
            else
                v.push_back(s[i]);
        }

        return v.size();
    }
};
```
