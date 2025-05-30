# Solution - 12 May 2025

---
## [2094. Finding 3-Digit Even Numbers](https://leetcode.com/problems/finding-3-digit-even-numbers)

### cpp
```cpp
class Solution {
public:
    void helper(int *cnt, vector<int> &ans, int cur = 0, int depth = 0) {
        if(depth == 3) {
            ans.push_back(cur);
            return;
        }
        int i=depth==0;
        while(i<10) {
            if(cnt[i]) {
                --cnt[i];
                helper(cnt, ans, cur * 10 + i, depth + 1);
                ++cnt[i];
            }
            depth == 2 ? i+=2 : ++i;
        }
    }

    vector<int> findEvenNumbers(vector<int>& digits) {
        int cnt[10] = {0};

        for(int digit:digits) cnt[digit]++;

        vector<int> ans;

        helper(cnt, ans);

        return ans;
    }
};
```
