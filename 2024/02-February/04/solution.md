# Solution - 04 Feb 2024

---
## [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring)

### cpp
```cpp
class Solution {
public:
    string minWindow(string s, string t) {
        int n=s.size(), m=t.size(), len=INT_MAX, start=0, cnt[128]={0}, count=0;
        
        for(auto ch:t) cnt[ch]++;

        for(int i=0, j=0; i<n; ++i) {
            cnt[s[i]]--;
            if(cnt[s[i]] >= 0) ++count;

            while(count == m) {
                if(i-j+1 < len)
                    len = i-j+1, start = j;
                cnt[s[j]]++;
                if(cnt[s[j]] > 0) --count;
                ++j;
            }
        }

        return len == INT_MAX ? "" : s.substr(start, len);
    }
};
```
