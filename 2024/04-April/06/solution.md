# Solution - 06 Apr 2024

---
## [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses)

### cpp
```cpp
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        stack<int> stk;
        for(int i=0; i<s.size(); ++i) {
            if(s[i]=='(') stk.push(i);
            else if(s[i]==')') {
                if(stk.size()) stk.pop();
                else s[i] = '*';
            }
        }

        while(stk.size()) 
            s[stk.top()]='*', stk.pop();

        string ans = "";
        for(int i=0; i<s.size(); ++i) 
            if(s[i]!='*') ans.push_back(s[i]);

        return ans;
    }
};
```
