# Solution - 20 Nov 2023

---
## [2391. Minimum Amount of Time to Collect Garbage](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage)

### cpp
```cpp
class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        int metal=0, paper=0, glass=0, mc=0, pc=0, gc=0;

        for(int i=0; i<garbage.size(); ++i) {
            if(i!=0) mc += travel[i-1], pc += travel[i-1], gc += travel[i-1];
            
            for(auto ch:garbage[i]) {
                if(ch=='M') ++mc, metal=mc;
                else if(ch=='P') ++pc, paper=pc;
                else ++gc, glass=gc;
            }
        }

        return metal+paper+glass;
    }
};
```
