# Solution - 30 Jul 2024

---
## [1653. Minimum Deletions to Make String Balanced](https://leetcode.com/problems/minimum-deletions-to-make-string-balanced)

### cpp
```cpp
class Solution {
public:
    int minimumDeletions(string s) {
        vector<int> pre(s.size()), post(s.size());
        pre[0] = (s[0]=='b');
        post.back() = (s.back()=='a');

        for(int i=1; i<s.size(); ++i)
            pre[i] = pre[i-1] + (s[i]=='b');
        
        for(int i=s.size()-2; i>=0; --i)
            post[i] = post[i+1] + (s[i]=='a');
        
        int ans = INT_MAX;
        for(int i=0; i<=s.size(); ++i)
            ans = min(ans, (i==0 ? post[i] : i==s.size() ? pre.back() : pre[i-1] + post[i]));
        
        return ans;
    }
};
```
