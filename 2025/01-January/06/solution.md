# Solution - 06 Jan 2025

---
## [1769. Minimum Number of Operations to Move All Balls to Each Box](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box)

### cpp
```cpp
class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();
        vector<int> ans(n);

        for(int i=0, ops=0, balls=0; i<n; ++i) {
            ans[i] += ops;
            balls += boxes[i] == '1';
            ops += balls;
        }

        for(int i=n-1, ops=0, balls=0; i>=0; --i) {
            ans[i] += ops;
            balls += boxes[i] == '1';
            ops += balls;
        }

        return ans;
    }
};
```
