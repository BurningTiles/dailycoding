# Solution - 01 Jan 2025

---
## [1422. Maximum Score After Splitting a String](https://leetcode.com/problems/maximum-score-after-splitting-a-string)

### cpp
```cpp
class Solution {
public:
    int maxScore(string s) {
        int n = s.size(), ltor[n], rtol[n], ans = 0;
        ltor[0] = s[0]=='0';
        rtol[n-1] = s[n-1]=='1';

        for(int i=n-2; i>=0; --i)
            rtol[i] = rtol[i+1] + (s[i] == '1');

        for(int i=1; i<n; ++i) {
            ans = max(ans, ltor[i-1] + rtol[i]);
            ltor[i] = ltor[i-1] + (s[i] == '0');
        }
        
        return ans;
    }
};
```
