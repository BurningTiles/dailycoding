# Solution - 01 May 2024

---
## [2000. Reverse Prefix of Word](https://leetcode.com/problems/reverse-prefix-of-word)

### cpp
```cpp
class Solution {
public:
    string reversePrefix(string word, char ch) {
        int n=0;

        while(n<word.size() && word[n]!=ch)
            ++n;
        
        if(n<word.size())
            reverse(word.begin(), word.begin()+n+1);

        return word;
    }
};
```
