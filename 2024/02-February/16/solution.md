# Solution - 16 Feb 2024

---
## [1481. Least Number of Unique Integers after K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals)

### cpp
```cpp
class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        unordered_map<int, int> count;
        vector<int> v; v.reserve(count.size());

        for(auto num:arr) 
            count[num]++;

        for(auto &cnt:count)
            v.push_back(cnt.second);
        
        sort(v.begin(), v.end());

        for(int i=0; i<v.size(); ++i)
            if(v[i] <= k) k -= v[i];
            else return v.size() - i;

        return 0;
    }
};
```
