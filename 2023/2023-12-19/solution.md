# Solution - 19 Dec 2023

---
## [661. Image Smoother](https://leetcode.com/problems/image-smoother)

### cpp
```cpp
class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        int m=img.size(), n=img[0].size();
        vector<vector<int>> ans(m, vector<int>(n, 0));

        for(int i=0; i<img.size(); ++i) {
            for(int j=0; j<img[i].size(); ++j) {
                int cnt = 0, sum = 0;

                for(int x=max(0, i-1); x<min(m, i+2); ++x)
                    for(int y=max(0, j-1); y<min(n, j+2); ++y)
                        ++cnt, sum += img[x][y];
                
                ans[i][j] = sum / cnt;
            }
        }

        return ans;
    }
};
```
