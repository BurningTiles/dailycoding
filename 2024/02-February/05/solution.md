# Solution - 05 Feb 2024

---
## [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string)

### cpp
```cpp
class Solution {
public:
    int firstUniqChar(string s) {
        int cnt[128]={0}, pos[128], ans = INT_MAX, n=s.size();
        
        for(int i=0; i<n; ++i)
            ++cnt[s[i]], pos[s[i]]=i;
        
        for(int i=97; i<123; ++i)
            if(cnt[i]==1)
                ans = min(ans, pos[i]);
        
        return ans==INT_MAX ? -1 : ans;
    }
};
```
