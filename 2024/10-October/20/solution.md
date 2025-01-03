# Solution - 20 Oct 2024

---
## [1106. Parsing A Boolean Expression](https://leetcode.com/problems/parsing-a-boolean-expression)

### cpp
```cpp
class Solution {
public:
    bool recSolver(string &exp, int &i) {
        int ans = -1;
        char op = exp[i];
        i += 2;

        while(i<exp.size()) {
            if(exp[i] == ')')
                break;
            else if(exp[i] != ',') {
                int val = exp[i] == 't' ? 1 : exp[i] == 'f' ? 0 : recSolver(exp, i);
                if(op == '!')
                    ans = !val;
                else if(ans == -1)
                    ans = val;
                else if(op == '&')
                    ans &= val;
                else if(op == '|')
                    ans |= val;
            }
            ++i;
        }

        return ans;
    }

    bool parseBoolExpr(string expression) {
        int i=0;
        return recSolver(expression, i);
    }
};
```
