# Solution - 17 Nov 2024

---
## [862. Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k)

### cpp
```cpp
class Solution {
public:
    int shortestSubarray(vector<int> &nums, int k) {
        long long n = nums.size(), sum = 0, ans = n+1, mx = -n-1;
        set<pair<long long, long long>> myset;
        myset.insert({0, -1});

        for(long long i=0; i<n; ++i) {
            sum += nums[i];
            myset.insert({sum, i});
            
            while(myset.begin()->first <= sum-k) {
                mx = max(mx, myset.begin()->second);
                myset.erase(myset.begin());
            }

            ans = min(ans, i-mx);
        }

        return ans>=n+1 ? -1 : ans;
    }
};
```
