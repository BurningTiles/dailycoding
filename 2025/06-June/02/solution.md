# Solution - 02 Jun 2025

---
## [135. Candy](https://leetcode.com/problems/candy)

### cpp
```cpp
class Solution {
public:
    // Two pass approach. O(n) space complexity.
    int candy1(vector<int>& ratings) {
        vector<int> count(ratings.size(), 1);

        for(int i=1; i<ratings.size(); ++i)
            if(ratings[i]>ratings[i-1]) count[i] = count[i-1] + 1;
        for(int i=ratings.size()-2; i>=0; --i) 
            if(ratings[i]>ratings[i+1]) count[i] = max(count[i], count[i+1] + 1);
        
        int ans = 0;
        for(auto &c:count) ans += c;
        return ans;
    }

    // One pass approach with O(1) space complexity.
    int candy(vector<int> &ratings) {
        if(!ratings.size()) return 0;

        int ans = 1, up = 0, down = 0, peak = 0;
        for(int i=1; i<ratings.size(); i++)
            if(ratings[i] > ratings[i-1]) 
                ++up, down=0, peak=up, ans += 1 + up;
            else if(ratings[i] < ratings[i-1]) 
                ++down, up=0, ans += 1 + down, peak >= down ? --ans : 0;
            else 
                up = down = peak = 0, ++ans;

        return ans;
    }
};
```
