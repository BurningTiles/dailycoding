# Solution - 27 Jun 2025

---
## [2014. Longest Subsequence Repeated k Times](https://leetcode.com/problems/longest-subsequence-repeated-k-times)

### cpp
```cpp
class Solution {
public:
    bool isK(string sub, string t, int k) {
        int count = 0, i = 0;

        for(char ch:t) {
            if(ch == sub[i]) {
                if(++i == sub.size()) {
                    i = 0;
                    if(++count == k) return true;
                }
            }
        }

        return false;
    }

    string longestSubsequenceRepeatedK(string s, int k) {
        string ans = "";
        queue<string> q;
        q.push("");

        while(q.size()) {
            string cur = q.front(); q.pop();
            
            for(char ch='a'; ch<='z'; ++ch) {
                string next = cur + ch;
                if(isK(next, s, k)) {
                    ans = next;
                    q.push(next);
                }
            }
        }

        return ans;
    }
};
```
