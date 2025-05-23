# Solution - 14 Mar 2025

---
## [2226. Maximum Candies Allocated to K Children](https://leetcode.com/problems/maximum-candies-allocated-to-k-children)

### cpp
```cpp
class Solution {
public:
    long long parts(vector<int> &candies, long long val) {
        if(val == 0) return LONG_MAX;
        long long cnt = 0;
        for(int i=0; i<candies.size(); ++i)
            cnt += candies[i]/val;
        return cnt;
    }

    int maximumCandies(vector<int>& candies, long long k) {
        long long total = 0, ans = 0;

        for(int i=0; i<candies.size(); ++i)
            total += candies[i];
        
        long long l=0, r=total/k;
        
        while(l<=r) {
            long long mid = (l+r) / 2, cnt = parts(candies, mid);

            if(cnt<k) 
                r = mid - 1;
            else {
                ans = mid;
                l = mid + 1;
            }
        }

        return ans;
    }
};
```
