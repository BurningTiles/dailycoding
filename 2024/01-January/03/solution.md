# Solution - 03 Jan 2024

---
## [2125. Number of Laser Beams in a Bank](https://leetcode.com/problems/number-of-laser-beams-in-a-bank)

### cpp
```cpp
class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int last=0, ans=0;
        for(auto &row:bank) {
            int device = count(row.begin(), row.end(), '1');
            if(device)
                ans += last * device, last = device;
        }
        return ans;
    }
};
```
