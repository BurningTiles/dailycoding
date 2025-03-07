# Solution - 12 Nov 2024

---
## [2070. Most Beautiful Item for Each Query](https://leetcode.com/problems/most-beautiful-item-for-each-query)

### cpp
```cpp
class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        vector<int> ans;
        sort(items.begin(), items.end());

        for(int i=1; i<items.size(); ++i)
            items[i][1] = max(items[i-1][1], items[i][1]);
        
        for(int i=0; i<queries.size(); ++i) {
            int l=0, r=items.size()-1, maxBeauty = 0, mid;
            
            while(l<=r) {
                mid = (l+r)/2;
                if(items[mid][0] <= queries[i]) {
                    maxBeauty = items[mid][1];
                    l = mid + 1;
                } else
                    r = mid - 1;
            }

            ans.push_back(maxBeauty);
        }

        return ans;
    }
};
```
