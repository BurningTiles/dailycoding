# Solution - 01 Oct 2023

---
## [1. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii)

### cpp
```cpp
class Solution {
public:
    void reverse(string &s, int i, int j) {
        while(i<j) swap(s[i++], s[j--]);
    }

    string reverseWords(string s) {
        int l=0;
        for(int i=0; i<s.size(); i++)
            if(s[i]==' ') reverse(s, l, i-1), l=i+1;
        reverse(s, l, s.size()-1);
        return s;
    }
};
```
