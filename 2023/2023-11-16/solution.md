# Solution - 16 Nov 2023

---
## [1980. Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string)

### cpp
```cpp
class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        string s(nums.size(), '0');
        for(int i=0; i<nums.size(); ++i)
            if(nums[i][i]=='0') s[i] = '1';
        return s;
    }
};
```
