# Solution - 25 May 2025

---
## [2942. Find Words Containing Character](https://leetcode.com/problems/find-words-containing-character)

### cpp
```cpp
class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> ans;

        for(int i=0; i<words.size(); ++i) {
            if(words[i].find(x) != string::npos)
                ans.push_back(i);
        }

        return ans;
    }
};
```
