# Solution - 08 Mar 2024

---
## [3005. Count Elements With Maximum Frequency](https://leetcode.com/problems/count-elements-with-maximum-frequency)

### cpp
```cpp
class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        int count[101] = {0}, freq=0, n=0;
        
        for(auto num:nums) ++count[num];
        for(auto cnt:count)
            if(cnt > freq) freq = cnt, n = 1;
            else if(cnt == freq) ++n;
        
        return freq * n;
    }
};
```
