# Solution - 10 Oct 2024

---
## [962. Maximum Width Ramp](https://leetcode.com/problems/maximum-width-ramp)

### cpp
```cpp
class Solution {
public:
    int maxWidthRamp(vector<int>& A) {
        stack<int> s;
        int res = 0, n = A.size();
        for (int i = 0; i < n; ++i)
            if (s.empty() || A[s.top()] > A[i])
                s.push(i);
        for (int i = n - 1; i > res; --i)
            while (!s.empty() && A[s.top()] <= A[i])
                res = max(res, i - s.top()), s.pop();
        return res;
    }
};
```
