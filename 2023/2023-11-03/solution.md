# Solution - 03 Nov 2023

---
## [1441. Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations)

### cpp
```cpp
class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        const string push = "Push", pop = "Pop";
        vector<string> ans;
        int t=0;
        for(int i=1; i<=target.back() && t<target.size(); i++)
            if(i==target[t]) ans.push_back(push), ++t;
            else ans.push_back(push), ans.push_back(pop);
        return ans;
    }
};
```
