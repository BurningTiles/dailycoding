# Solution - 29 Oct 2023

---
## [458. Poor Pigs](https://leetcode.com/problems/poor-pigs) 

### cpp
```cpp
class Solution {
public:
    int poorPigs(int buckets, int poisonTime, int totalTime) {
        return ceil(log2(buckets) / log2(totalTime / poisonTime + 1));
    }
};
```
