# Solution - 19 Jul 2025

---
## [1233. Remove Sub-Folders from the Filesystem](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem)

### cpp
```cpp
class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        sort(folder.begin(), folder.end());
        vector<string> ans = {folder[0]};

        for(int i=1; i<folder.size(); ++i) {
            string last = ans.back() + "/";

            if(folder[i].compare(0, last.size(), last) != 0)
                ans.push_back(folder[i]);
        }

        return ans;
    }
};
```
