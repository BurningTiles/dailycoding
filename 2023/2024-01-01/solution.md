# Solution - 01 Jan 2024

---
## [455. Assign Cookies](https://leetcode.com/problems/assign-cookies)

### cpp
```cpp
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int ans=0, i=0, j=0;
        while(i<g.size() && j<s.size()) {
            if(g[i]<=s[j]) ++ans, ++i, ++j;
            else ++j;
        }
        return ans;
    }
};
```
