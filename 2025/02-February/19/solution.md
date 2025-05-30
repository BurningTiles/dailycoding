# Solution - 19 Feb 2025

---
## [1415. The k-th Lexicographical String of All Happy Strings of Length n](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n)

### cpp
```cpp
class Solution {
public:
    void helper(int len, string &str, vector<string> &ans) {
        if (str.size() >= len) {
            ans.push_back(str);
            return;
        }

        char last = str.size() ? str.back() : 'x';
        for (char ch='a'; ch<'d'; ++ch) {
            if (ch == last)
                continue;
            str.push_back(ch);
            helper(len, str, ans);
            str.pop_back();
        }
    }

    string getHappyString(int n, int k) {
        vector<string> ans;
        string str = "";

        helper(n, str, ans);

        return k <= ans.size() ? ans[k-1] : "";
    }
};
```
