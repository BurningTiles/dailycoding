# Solution - 05 Sep 2024

---
## [2028. Find Missing Observations](https://leetcode.com/problems/find-missing-observations)

### cpp
```cpp
class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int requiredSum = mean * (rolls.size() + n);
        
        for(int i=0; i<rolls.size(); ++i)
            requiredSum -= rolls[i];

        if(requiredSum < n || requiredSum > (n*6))
            return {};
        
        int per = requiredSum / n, ext = requiredSum % n;
        vector<int> ans(n, per);

        for(int i=0; i<ext; ++i)
            ++ans[i];

        return ans;
    }
};
```
