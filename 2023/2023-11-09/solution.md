# Solution - 09 Nov 2023

---
## [1759. Count Number of Homogenous Substrings](https://leetcode.com/problems/count-number-of-homogenous-substrings)

### cpp
```cpp
class Solution {
public:
    int countHomogenous(string s) {
        ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
        long long cnt = 0, ans = 0;
        for(int i=0; i<s.size(); ++i) {
            if(i>0 && s[i]==s[i-1]) ++cnt;
            else cnt = 1;
            ans += cnt;
        }
        return ans % 1000000007;
    }
};
```
