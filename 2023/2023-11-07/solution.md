# Solution - 07 Nov 2023

---
## [1921. Eliminate Maximum Number of Monsters](https://leetcode.com/problems/eliminate-maximum-number-of-monsters)

### cpp
```cpp
class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        int n=dist.size(), tmp;
        vector<int> time(n, 0);
        for(int i=0; i<n; i++) {
            tmp = ceil(double(dist[i]) / speed[i]);
            if(tmp < n) time[tmp]++;
        }

        int killed = 0;
        for(int i=0; i<time.size(); i++) {
            if(killed + time[i] > i) 
                return i;
            killed += time[i];
        }
        return n;
    }
};
```
