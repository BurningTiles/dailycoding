# Solution - 13 Apr 2024

---
## [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle)

### cpp
```cpp
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int ans = 0;
        vector<int> h(matrix[0].size()+1, 0);

        for(int i=0; i<matrix.size(); ++i) {
            for(int j=0; j<matrix[0].size(); ++j)
                h[j] = matrix[i][j]=='1' ? h[j]+1 : 0;
            ans = max(ans, largestRectangleArea(h));
        }
        
        return ans;
    }

    int largestRectangleArea(vector<int> &heights) {
        int ans = 0;
        stack<int> stk;

        for(int i=0; i<heights.size(); ++i) {
            while(stk.size() && heights[stk.top()] >= heights[i]) {
                int h = heights[stk.top()]; stk.pop();
                ans = max(ans, h*(stk.size() ? i-stk.top()-1 : i));
            }
            stk.push(i);
        }

        return ans;
    }
};
```
