# Solution - 09 Jul 2024

---
## [1701. Average Waiting Time](https://leetcode.com/problems/average-waiting-time)

### cpp
```cpp
class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        long long waiting = 0, time = 0;
        
        for(auto &cust:customers) {
            if(cust[0] >= time) 
                waiting += cust[1], time = cust[0] + cust[1];
            else
                waiting += time +cust[1] - cust[0], time += cust[1];
        }

        return double(waiting)/customers.size();
    }
};
```
