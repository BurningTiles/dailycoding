# Solution - 22 May 2024

---
## [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning)

### cpp
```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> ans;
        vector<string> cur;
        helper(s, ans, cur);
        return ans;
    }

    void helper(string &s, vector<vector<string>> &ans, vector<string> &cur, int i=0) {
        if(i==s.size())
            ans.push_back(cur);
        
        string str = "";
        for(int j=i; j<s.size(); ++j) {
            if(isPalindrome(str += s[j])) {
                cur.push_back(str);
                helper(s, ans, cur, j+1);
                cur.pop_back();
            }
        }
    }

    bool isPalindrome(string &s) {
        for(int i=0, j=s.size()-1; i<j; ++i, --j)
            if(s[i]!=s[j])
                return false;
        return true;
    }
};
```
