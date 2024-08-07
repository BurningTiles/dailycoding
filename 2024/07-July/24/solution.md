# Solution - 24 Jul 2024

---
## [2191. Sort the Jumbled Numbers](https://leetcode.com/problems/sort-the-jumbled-numbers)

### cpp
```cpp
class Solution {
public:
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        vector<vector<int>> v;
        vector<int> ans;

        for(int i=0; i<nums.size(); ++i) {
            int tmp = nums[i], mapped = 0, mul = 1, digit;
            do {
                digit = tmp%10, tmp /= 10;
                mapped += mul * (mapping[digit]);
                mul *= 10;
            } while(tmp);
            v.push_back({mapped, i, nums[i]});
        }

        sort(v.begin(), v.end());

        for(auto &p:v)
            ans.push_back(p[2]);

        return ans;
    }
};
```
