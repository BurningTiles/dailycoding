# Solution - 02 Feb 2024

---
## [1291. Sequential Digits](https://leetcode.com/problems/sequential-digits)

### cpp
```cpp
class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int> ans;

        for(int i=1; i<10; ++i) {
            long long num = i, next = i+1;

            while(num <= high && next <= 9) {
                num = num * 10 + next;
                if(num >= low && num <= high)
                    ans.push_back(num);
                ++next;
            }
        }

        sort(ans.begin(), ans.end());
        return ans;
    }
};
```
