# Solution - 04 Sep 2024

---
## [874. Walking Robot Simulation](https://leetcode.com/problems/walking-robot-simulation)

### cpp
```cpp
class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        unordered_set<string> uset;

        for(auto obs:obstacles)
            uset.insert(to_string(obs[0]) + " " + to_string(obs[1]));
        
        int dirs[] = {0, 1, 0, -1, 0};
        int d = 0, x = 0, y = 0, ans = 0;

        for(auto com:commands) {
            if(com == -1)
                ++d;
            else if(com == -2)
                --d;
            else {
                while(com-- > 0) {
                    string tmp = to_string(x + dirs[d]) + " " + to_string(y + dirs[d+1]);
                    if(uset.count(tmp)) break;
                    x += dirs[d];
                    y += dirs[d+1];
                }
            }

            ans = max(ans, x*x + y*y);

            if(d == 4) d = 0;
            if(d == -1) d = 3;
        }

        return ans;
    }
};
```
