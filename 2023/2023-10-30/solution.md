# Solution - 30 Oct 2023

---
## [1356. Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits)

### cpp
```cpp
class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        pair<int, int> a[arr.size()];
        for(int i=0; i<arr.size(); i++) {
            int tmp = arr[i], cnt=0;
            while(tmp)
                cnt += tmp&1, tmp/=2;
            a[i] = {cnt, arr[i]};
        }
        sort(a, a+arr.size());
        for(int i=0; i<arr.size(); i++)
            arr[i] = a[i].second;
        return arr;
    }
};
```
