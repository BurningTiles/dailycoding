# Solution - 01 Dec 2023

---
## [1662. Check If Two String Arrays are Equivalent](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent)

### cpp
```cpp
class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        int i=0, j=0, x=0, y=0; 
        while(i<word1.size() && j<word2.size()) {
            if(word1[i][x] != word2[j][y]) return false;
            x++, y++;
            if(x==word1[i].size()) ++i, x=0;
            if(y==word2[j].size()) ++j, y=0;
        }
        return i==word1.size() && j==word2.size();
    }
};
```
