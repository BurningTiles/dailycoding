# Solution - 26 May 2024

---
## [552. Student Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii)

### cpp
```cpp
class Solution {
public:
    int checkRecord(int n) {
        vector<int> dp = {1, 1, 0, 1, 0, 0};
        for(int i=2; i<=n; ++i)
            dp = {sum(dp, 0, 2), dp[0], dp[1], sum(dp, 0, 5), dp[3], dp[4]};
        return sum(dp, 0, 5);
    }

    int sum(vector<int> &a, int left, int right) {
        int ans = 0;
        for(int i=left; i<=right; ++i)
            ans = (ans + a[i]) % 1000000007;
        return ans;
    }
};
```
