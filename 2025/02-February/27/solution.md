# Solution - 27 Feb 2025

---
## [873. Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence)

### cpp
```cpp
class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        unordered_map<int, int> m;
        int N = arr.size(), ans = 0;
        int dp[N][N];

        for (int j = 0; j < N; ++j) {
            m[arr[j]] = j;
            
            for (int i = 0; i < j; ++i) {
                int k = m.find(arr[j] - arr[i]) == m.end() ? -1 : m[arr[j] - arr[i]];
                dp[i][j] = (arr[j] - arr[i] < arr[i] && k >= 0) ? dp[k][i] + 1 : 2;
                ans = max(ans, dp[i][j]);
            }
        }
        
        return ans > 2 ? ans : 0;
    }
};
```
