# Solution - 18 Aug 2024

---
## [264. Ugly Number II](https://leetcode.com/problems/ugly-number-ii)

### cpp
```cpp
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> ans = {1};
        int i=0, j=0, k=0;
        
        while(ans.size() < n) {
            ans.push_back(min(ans[i]*2, min(ans[j]*3, ans[k]*5)));
            if(ans.back() == ans[i] * 2) ++i;
            if(ans.back() == ans[j] * 3) ++j;
            if(ans.back() == ans[k] * 5) ++k;
        }

        return ans.back();
    }
};
```
