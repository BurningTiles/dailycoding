# Solution - 18 Apr 2025

---
## [38. Count and Say](https://leetcode.com/problems/count-and-say)

### cpp
```cpp
class Solution {
public:
    string countAndSay(int n) {
        string ans = "1";

        for(int i=1; i<n; i++) {
            string tmp = "";
            int count = 1;
            for(int j=1; j<ans.size(); j++)
                if(ans[j]==ans[j-1]) ++count;
                else {
                    tmp += to_string(count) + ans[j-1];
                    count = 1;
                }
            tmp += to_string(count) + ans.back();
            ans = tmp;
        }
        
        return ans;
    }
};
```
