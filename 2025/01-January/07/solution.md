# Solution - 07 Jan 2025

---
## [1408. String Matching in an Array](https://leetcode.com/problems/string-matching-in-an-array)

### cpp
```cpp
class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        vector<string> ans;

        for(int i=0; i<words.size(); ++i) {
            for(int j=0; j<words.size(); ++j) {
                if(i != j && words[j].find(words[i]) != -1) {
                    ans.push_back(words[i]);
                    break;
                }
            }
        }

        return ans;
    }
};
```
