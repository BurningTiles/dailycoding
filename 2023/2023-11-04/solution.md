# Solution - 04 Nov 2023

---
## [1503. Last Moment Before All Ants Fall Out of a Plank](https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank)

### cpp
```cpp
class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        int ans = INT_MIN;
        for(int i=0; i<left.size(); i++)
            ans = max(ans, left[i]);
        for(int i=0; i<right.size(); i++)
            ans = max(ans, n-right[i]);
        return ans;
    }
};
```
