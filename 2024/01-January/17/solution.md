# Solution - 17 Jan 2024

---
## [1207. Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences)

### cpp
```cpp
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        int cnt[2001] = {0}, mark[1001] = {0};
        for(auto num:arr)
            cnt[num+1000]++;
        
        for(int i=0; i<2000; ++i)
            if(cnt[i]) {
                if(mark[cnt[i]]) return false;
                mark[cnt[i]] = 1;
            }
        
        return true;
    }
};
```
