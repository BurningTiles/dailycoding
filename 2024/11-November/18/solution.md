# Solution - 18 Nov 2024

---
## [1652. Defuse the Bomb](https://leetcode.com/problems/defuse-the-bomb)

### cpp
```cpp
class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        vector<int> ans(n, 0);

        for(int i=0; i<n; ++i) {
            if(k > 0) {
                for(int j=1; j<=k; ++j)
                    ans[i] += code[(i+j) % n];
            } else if(k < 0) {
                for(int j=-1; j>=k; --j)
                    ans[i] += code[(i+j+n) % n];
            }
        }

        return ans;
    }
};
```
