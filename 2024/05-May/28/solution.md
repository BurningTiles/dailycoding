# Solution - 28 May 2024

---
## [1208. Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget)

### cpp
```cpp
class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int ans = 0, cost = 0, j = 0;

        for(int i=0; i<s.size(); ++i) {
            cost += abs(t[i]-s[i]);

            while(j <= i && cost > maxCost) {
                cost -= abs(t[j]-s[j]);
                ++j;
            }
            
            ans = max(ans, i-j+1);
        }

        return ans;
    }
};
```
