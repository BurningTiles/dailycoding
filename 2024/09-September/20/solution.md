# Solution - 20 Sep 2024

---
## [214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome)

### cpp
```cpp
class Solution {
public:
    string shortestPalindrome(string s) {
        string rev = s;
        reverse(rev.begin(), rev.end());
        string l = s + "#" + rev;

        vector<int> prefix(l.size(), 0);
        for(int i=1; i<l.size(); ++i) {
            int j=prefix[i-1];
            while(j > 0 && l[i] != l[j])
                j = prefix[j-1];
            
            prefix[i] = (j += l[i] == l[j]);
        }

        return rev.substr(0, s.size() - prefix[l.size()-1]) + s;
    }
};
```
