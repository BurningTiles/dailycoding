# Solution - 03 Dec 2024

---
## [2109. Adding Spaces to a String](https://leetcode.com/problems/adding-spaces-to-a-string)

### cpp
```cpp
class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string ans(s.size() + spaces.size(), ' ');
        spaces.push_back(INT_MAX);

        for(int i=0, j=0, k=0; i<s.size(); ++i, ++k) {
            if(spaces[j] < i) ++j;
            if(spaces[j]==i) k++;
            ans[k] = s[i];
        }

        return ans;
    }
};
```
