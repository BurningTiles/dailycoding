# Solution - 09 Oct 2024

---
## [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid)

### cpp
```cpp
class Solution {
public:
    int minAddToMakeValid(string s) {
        int cnt = 0, ans = 0;

        for(int i=0; i<s.size(); ++i) {
            if(s[i] == '(') ++cnt;
            else {
                if(!cnt) ++ans;
                else --cnt;
            }
        }
        ans += cnt;

        return ans;
    }
};
```
