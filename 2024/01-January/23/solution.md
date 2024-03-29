# Solution - 23 Jan 2024

---
## [1239. Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters)

### cpp
```cpp
class Solution {
public:
    void helper(vector<string> &arr, bool mark[], int &ans, int i=0) {
        if(i==arr.size()) {
            int cnt = count(mark, mark+26, true);
            ans = max(ans, cnt);
            return;
        }

        helper(arr, mark, ans, i+1);
        int valid = true, j=0;
        for(; j<arr[i].size(); ++j) {
            if(mark[arr[i][j]-'a']) {
                valid = false;
                break;
            }
            mark[arr[i][j]-'a'] = true;
        }

        if(j == arr[i].size())
            helper(arr, mark, ans, i+1);
        
        --j;
        while(j >= 0)
            mark[arr[i][j]-'a'] = false, --j;
    }

    int maxLength(vector<string>& arr) {
        int ans = 0;
        bool mark[26] = {false};
        helper(arr, mark, ans);
        return ans;
    }
};
```
