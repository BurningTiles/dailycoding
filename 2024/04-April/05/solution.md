# Solution - 05 Apr 2024

---
## [1544. Make The String Great](https://leetcode.com/problems/make-the-string-great)

### cpp
```cpp
class Solution {
public:
    string makeGood(string s) {
        string ans = "";

        for(int i=0; i<s.size(); ++i)
            if(ans.size() && abs(ans.back()-s[i]) == 32) ans.pop_back();
            else ans.push_back(s[i]);
        
        return ans;
    }
};
```
