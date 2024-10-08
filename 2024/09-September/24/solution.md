# Solution - 24 Sep 2024

---
## [3043. Find the Length of the Longest Common Prefix](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix)

### cpp
```cpp
class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        unordered_set<int> uset;
        int ans = 0;

        for(int i=0; i<arr1.size(); ++i){
            while(arr1[i]) {
                uset.insert(arr1[i]);
                arr1[i] /= 10;
            }
        }

        for(int i=0; i<arr2.size(); ++i) {
            while(arr2[i]) {
                if(uset.contains(arr2[i])) {
                    ans = max(ans, (int) to_string(arr2[i]).size());
                    break;
                }
                arr2[i] /= 10;
            }
        }

        return ans;
    }
};
```
