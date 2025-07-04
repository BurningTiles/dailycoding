# Solution - 03 Jun 2025

---
## [1298. Maximum Candies You Can Get from Boxes](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes)

### cpp
```cpp
class Solution {
public:
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) {
        int ans = 0, i;
        queue<int> q;

        for(int i: initialBoxes)
            if((status[i] += 5000) > 5000)
                q.push(i);
        
        while(q.size()) {
            i = q.front(), q.pop();
            ans += candies[i];

            for(int j:keys[i])
                if((status[j] += 5) == 5005)
                    q.push(j);
            
            for(int j:containedBoxes[i])
                if((status[j] += 5000) > 5000)
                    q.push(j);
        }

        return ans;
    }
};
```
