# Solution - 24 Nov 2023

---
## [1561. Maximum Number of Coins You Can Get](https://leetcode.com/problems/maximum-number-of-coins-you-can-get)

### cpp
```cpp
auto init = [](){ios::sync_with_stdio(0); cin.tie(0); cout.tie(0); return 0;}();

class Solution {
public:
    int maxCoins(vector<int>& piles) {
        vector<int> count(10001, 0);
        int j = 0, ans=0, cp=piles.size()/3;
        
        for(int i=0; i<piles.size(); i++)
            count[piles[i]]++,
            j = max(j, piles[i]);

        bool myturn = false;
        while(j>0 && cp>0) {
            if(count[j]==0) --j;
            else {
                if(myturn) ans += j, cp--;
                --count[j];
                myturn = !myturn;
            }
        }

        return ans;
    }
};
```
