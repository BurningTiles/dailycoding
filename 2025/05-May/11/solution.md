# Solution - 11 May 2025

---
## [1550. Three Consecutive Odds](https://leetcode.com/problems/three-consecutive-odds)

### cpp
```cpp
class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        for(int i=0, j=0, cnt=0; i<arr.size(); ++i) {
            cnt += arr[i] & 1;
            if(cnt >= 3)
                return true;
            if(i-j+1 >= 3)
                cnt -= arr[j++] & 1;
        }

        return false;
    }
};
```
