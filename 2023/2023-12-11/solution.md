# Solution - 11 Dec 2023

---
## [1287. Element Appearing More Than 25% In Sorted Array](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array)

### cpp
```cpp
class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int cnt=1, req=arr.size()/4;
        for(int i=0; i<arr.size(); i++) {
            if(i>0 && arr[i]==arr[i-1]) ++cnt;
            else cnt = 1;
            if(cnt > req)
                return arr[i];
        }
        return 0;
    }
};
```
