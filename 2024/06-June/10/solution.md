# Solution - 10 Jun 2024

---
## [1051. Height Checker](https://leetcode.com/problems/height-checker)

### cpp
```cpp
class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> expected = heights;
        sort(expected.begin(), expected.end());

        int ans = 0;
        for(int i=0; i<heights.size(); ++i)
            if(heights[i] != expected[i]) ++ans;
            
        return ans;
    }
};
```
