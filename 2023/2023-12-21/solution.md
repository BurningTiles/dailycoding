# Solution - 21 Dec 2023

---
## [1637. Widest Vertical Area Between Two Points Containing No Points](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points)

### cpp
```cpp
class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        int arr[points.size()];
        
        for(int i=0; i<points.size(); i++)
            arr[i] = points[i][0];
        
        sort(arr, arr+points.size());

        int ans=0;
        for(int i=1; i<points.size(); i++)
            ans = max(ans, arr[i]-arr[i-1]);
        
        return ans;
    }
};
```
