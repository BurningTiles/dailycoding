# Solution - 13 Nov 2023

---
## [2785. Sort Vowels in a String](https://leetcode.com/problems/sort-vowels-in-a-string)

### cpp
```cpp
class Solution {
public:
    string sortVowels(string s) {
        const string vowels = "aeiouAEIOU";
        int count[128] = {0}, id=0;

        for(int i=0; i<s.size(); i++)
            if(vowels.find(s[i]) != -1)
                count[s[i]]++, s[i]=0;

        for(int i=0; i<s.size(); i++)
            if(s[i] == 0) {
                while(!count[id]) ++id;
                s[i] = id, count[id]--;
            }

        return s;
    }
};
```
