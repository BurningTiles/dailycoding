# Solution - 11 Apr 2024

---
## [402. Remove K Digits](https://leetcode.com/problems/remove-k-digits)

### cpp
```cpp
class Solution {
public:
    string removeKdigits(string num, int k) {
        string ans = "";

        for(int i=0; i<num.size(); ++i) {
            while(k && ans.size() && num[i] < ans.back())
                ans.pop_back(), --k;

            if(ans.size() || num[i]!='0')
                ans.push_back(num[i]);
        }

        while(ans.size() && k--) ans.pop_back();

        return ans == "" ? "0" : ans;
    }
};
```
