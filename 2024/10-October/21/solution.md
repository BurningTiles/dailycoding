# Solution - 21 Oct 2024

---
## [1593. Split a String Into the Max Number of Unique Substrings](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings)

### cpp
```cpp
class Solution {
public:
    void backtrack(string &s, unordered_set<string> &uset, int i, int cur, int &ans) {
        if(i == s.size()) {
            ans = max(ans, cur);
            return;
        }

        string tmp = "";
        do {
            tmp.push_back(s[i]);
            if(!uset.count(tmp)) {
                uset.insert(tmp);
                backtrack(s, uset, i+1, cur+1, ans);
                uset.erase(tmp);
            }
            ++i;
        } while(i < s.size());
    }

    int maxUniqueSplit(string s) {
        unordered_set<string> uset;
        int ans = 0;
        backtrack(s, uset, 0, 0, ans);
        return ans;
    }
};
```
