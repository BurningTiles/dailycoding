# Solution - 25 Dec 2023

---
## [91. Decode Ways](https://leetcode.com/problems/decode-ways)

### cpp
```cpp
class Solution {
public:
    int numDecodings(string s) {
        if(s.front() == '0') return false;

        int dp[s.size()+1];
        dp[0] = dp[1] = 1;

        for(int i=1; i<s.size(); i++) {
            dp[i+1] = 0;

            if(s[i] != '0') 
                dp[i+1] += dp[i];
            if(s[i-1]=='1' || (s[i-1]=='2' && s[i]<='6'))
                dp[i+1] += dp[i-1];

            if(!dp[i+1]) return 0;
        }

        return dp[s.size()];
    }
};
```
