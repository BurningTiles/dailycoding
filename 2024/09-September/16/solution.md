# Solution - 16 Sep 2024

---
## [539. Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference)

### cpp
```cpp
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        int ans = INT_MAX;
        vector<int> v;

        for(auto time:timePoints)
            v.push_back(((time[0]-'0') * 10 + time[1]-'0') * 60 + (time[3]-'0') * 10 + time[4]-'0');

        sort(v.begin(), v.end());
        v.push_back(v[0] + 1440);

        for(int i=1; i<v.size(); ++i)
            ans = min(ans, v[i]-v[i-1]);
        
        return ans;
    }
};
```
