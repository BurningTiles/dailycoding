# Solution - 06 Aug 2024

---
## [3016. Minimum Number of Pushes to Type Word II](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii)

### cpp
```cpp
class Solution {
public:
    int minimumPushes(string word) {
        int cnt[26] = {0};

        for(auto ch:word)
            cnt[ch-'a']++;
        
        sort(cnt, cnt+26, greater<int>());

        int ans = 0;
        for(int i=0; i<26 && cnt[i]>0; ++i)
            ans += cnt[i] * (i/8 + 1);

        return ans;
    }
};
```
