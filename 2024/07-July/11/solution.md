# Solution - 11 Jul 2024

---
## [1190. Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses)

### cpp
```cpp
class Solution {
public:
    string reverseParentheses(string s) {
        stack<string> stk;
        string cur = "";

        for(int i=0; i<s.size(); ++i) {
            if(s[i] == '(') {
                stk.push(cur), cur = "";
            }
            else if(s[i] == ')') {
                reverse(cur.begin(), cur.end());
                cur = stk.top() + cur;
                stk.pop();
            }
            else
                cur.push_back(s[i]);
        }

        return cur;
    }
};
```
