# Solution - 30 Jan 2024

---
## [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation)

### cpp
```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        const string op = "+-*/";
        for(auto &token:tokens) {
            if(op.find(token) != -1) {
                int b = stk.top(); stk.pop();
                int a = stk.top(); stk.pop();
                if(token=="+") stk.push(a+b);
                if(token=="-") stk.push(a-b);
                if(token=="*") stk.push(a*b);
                if(token=="/") stk.push(a/b);
            }
            else
                stk.push(stoi(token));
        }
        return stk.top();
    }
};
```
