# Solution - 18 Sep 2024

---
## [179. Largest Number](https://leetcode.com/problems/largest-number)

### cpp
```cpp
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        auto cmp = [&](int a, int b) {
            string sa = to_string(a), sb = to_string(b);
            return (sa + sb) > (sb + sa);
        };

        sort(nums.begin(), nums.end(), cmp);

        if(nums[0] == 0) return "0";

        string ans = "";
        for(int i=0; i<nums.size(); ++i)
            ans += to_string(nums[i]);
        
        return ans;
    }
};  
```
