# Solution - 28 Nov 2023

---
## [2147. Number of Ways to Divide a Long Corridor](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor)

### cpp
```cpp
auto init = [](){ios::sync_with_stdio(0); cin.tie(0); cout.tie(0); return 0;}();
class Solution {
public:
    int numberOfWays(string &corridor) {
        long long ans = 0, one = 0, two = 1;
        
        for(int i=0; i<corridor.size(); i++) {
            if(corridor[i]=='S')
                ans = one, swap(one, two);
            else
                two = (two + ans) % 1000000007;
        }

        return ans;
    }
};
```
