# Solution - 13 Jul 2024

---
## [2751. Robot Collisions](https://leetcode.com/problems/robot-collisions)

### cpp
```cpp
class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        int n = positions.size();
        vector<int> ind(n), stack, ans;

        for(int i=0; i<n; ++i)
            ind[i] = i;
        
        sort(ind.begin(), ind.end(), [&](int a, int b) {
            return positions[a] < positions[b];
        });

        for(auto i:ind) {
            if(directions[i] == 'R') {
                stack.push_back(i);
                continue;
            }

            while(stack.size() && healths[i] > 0) {
                if(healths[stack.back()] < healths[i]) {
                    healths[stack.back()] = 0, stack.pop_back();
                    healths[i] -= 1;
                } else if(healths[stack.back()] > healths[i]) {
                    healths[stack.back()] -= 1;
                    healths[i] = 0;
                } else {
                    healths[stack.back()] = 0, stack.pop_back();
                    healths[i] = 0;
                }
            }
        }

        for(auto h:healths)
            if(h > 0) ans.push_back(h);
        
        return ans;
    }
};
```
