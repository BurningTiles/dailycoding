# Solution - 16 Dec 2023

---
## [242. Valid Anagram](https://leetcode.com/problems/valid-anagram)

### cpp
```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;
        int count[128] = {0};
        
        for(auto ch:s) count[ch]++;
        
        for(auto ch:t)
            if(!count[ch]--)
                return false;
        
        for(int i='a'; i<='z'; i++)
            if(count[i])
                return false;
        
        return true;
    }
};
```
