# Solution - 11 Feb 2025

---
## [1910. Remove All Occurrences of a Substring](https://leetcode.com/problems/remove-all-occurrences-of-a-substring)

### cpp
```cpp
class Solution {
public:
    bool ends_with(string &s1, string &s2) {
        if(s1.size() < s2.size()) return false;
        int l1=s1.size()-1, l2=s2.size()-1;

        while(l2 >= 0 && s2[l2] == s1[l1])
            --l2, --l1;
        
        return l2 == -1;
    }

    string removeOccurrences(string s, string part) {
        string tmp = "";

        for(int i=0; i<s.size(); ++i) {
            tmp.push_back(s[i]);
            if(ends_with(tmp, part))
                for(int j=0; j<part.size(); ++j)
                    tmp.pop_back();
        }

        return tmp;
    }
};
```
