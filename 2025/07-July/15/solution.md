# Solution - 15 Jul 2025

---
## [3136. Valid Word](https://leetcode.com/problems/valid-word)

### cpp
```cpp
class Solution {
public:
    bool isValid(string word) {
        if(word.size() < 3) return false;
        int hasVowel = false, hasConsonant = false;
        const string vowels = "AEIOUaeiou";

        for(char ch:word) {
            if(!((ch>='A' && ch<='Z') || (ch>='a' && ch<='z') || (ch>='0' && ch<='9')))
                return false;
            if(vowels.find(ch) != -1)
                hasVowel = true;
            else if(ch > '9')
                hasConsonant = true;
        }

        return hasVowel && hasConsonant;
    }
};
```
