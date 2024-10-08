# Solution - 19 Sep 2024

---
## [241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses)

### cpp
```cpp
class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        vector<int> ans;
        int n = expression.size();
        const string ops = "+-*";

        for(int i=0; i<n; ++i) {
            char ch = expression[i];

            if(ops.find(ch) != -1) {
                vector<int> ans1 = diffWaysToCompute(expression.substr(0, i));
                vector<int> ans2 = diffWaysToCompute(expression.substr(i+1));

                for(int a: ans1)
                    for(int b: ans2)
                        if(ch == '+')
                            ans.push_back(a + b);
                        else if(ch == '-')
                            ans.push_back(a - b);
                        else
                            ans.push_back(a * b);
            }
        }

        if(ans.empty())
            ans.push_back(stoi(expression));

        return ans;
    }
};
```
