# Solution - 10 Dec 2024

---
## [2981. Find Longest Special Substring That Occurs Thrice I](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i)

### cpp
```cpp
class Solution {
public:
    bool helper(string &s, int n, int x) {
        vector<int> cnt(26, 0);
        int j = 0;

        for(int i=0; i<n; ++i) {
            while(s[i] != s[j]) ++j;
            if (i-j+1 >= x) cnt[s[i]-'a']++;
            if (cnt[s[i]-'a'] > 2) return true;
        }

        return false;
    }

    int maximumLength(string s) {
        int n = s.size(), l = 1, r = n;

        if(!helper(s, n, l)) return -1;

        while(l + 1 < r) {
            int mid = (l + r) / 2;
            if(helper(s, n, mid)) l = mid;
            else r = mid;
        }

        return l;
    }
};
```
