# Solution - 01 Jul 2024

---
## [1550. Three Consecutive Odds](https://leetcode.com/problems/three-consecutive-odds)

### cpp
```cpp
class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int n = arr.size(), cnt=0;
        for(int i=0; i<n; ++i) {
            if(arr[i]&1) ++cnt;
            else cnt=0;
            if(cnt>2) return true;
        }
        return false;
    }
};
```
