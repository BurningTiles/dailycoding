# Solution - 06 Apr 2025

---
## [368. Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset)

### cpp
```cpp
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size(), dp[n], track[n], maxLen = 0, end = 0;
        dp[0] = 1, track[0] = 0;

        for(int i=1; i<n; ++i) {
            track[i] = i, dp[i] = 1;
            
            for(int j=0; j<i; ++j) {
                if(nums[i]%nums[j] == 0 && dp[j]+1 > dp[i])
                    dp[i] = dp[j]+1, track[i] = j;
            }

            if(dp[i] > maxLen)
                maxLen = dp[i], end = i;
        }

        vector<int> ans = {nums[end]};
        while(track[end] != end)
            end = track[end],
            ans.push_back(nums[end]);
        
        return ans;
    }

    /*
    // Old version
    vector<int> largestDivisibleSubset1(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        sort(nums.begin(), nums.end());
        vector<vector<int>> v(n+1);

        for(int i=1; i<=n; ++i) {
            int curMax = 0;

            for(int j=1; j<i; ++j)
                if(nums[i-1] % nums[j-1] == 0 && v[j].size() > v[curMax].size())
                    curMax = j;

            v[i] = v[curMax];
            v[i].push_back(nums[i-1]);

            if(v[ans].size() < v[i].size())
                ans = i;
        }

        return v[ans];
    }
    */
};
```
