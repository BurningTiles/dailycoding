# Solution - 21 Jul 2025

---
## [1957. Delete Characters to Make Fancy String](https://leetcode.com/problems/delete-characters-to-make-fancy-string)

### cpp
```cpp
class Solution {
public:
    string makeFancyString(string s) {
        int last = 0, last1 = 0;
        string ans = "";
        
        for(int i=0; i<s.size(); ++i) {
            if(s[i]==last && s[i]==last1)
                continue;
            ans.push_back(s[i]);
            last1 = last;
            last = ans.back();
        }

        return ans;
    }
};
```
