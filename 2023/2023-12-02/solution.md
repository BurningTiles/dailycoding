# Solution - 02 Dec 2023

---
## [1160. Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters)

### cpp
```cpp
class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int count[26] = {0}, ans = 0;

        for(auto ch:chars)
            count[ch-'a']++;
        
        for(auto &word:words) {
            int wordCount[26] = {0}, flag = true;
            for(auto ch:word) {
                wordCount[ch-'a']++;
                if(wordCount[ch-'a'] > count[ch-'a']) {
                    flag = false; break;
                }
            }

            if(flag)
                ans += word.size();
        }

        return ans;
    }
};
```
