# Solution - 08 Jun 2025

---
## [386. Lexicographical Numbers](https://leetcode.com/problems/lexicographical-numbers)

### cpp
```cpp
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans;
        int num = 1;

        for(int i=0; i<n; ++i) {
            ans.push_back(num);

            if(num *10 <= n)
                num *= 10;
            else {
                while(num % 10 == 9 || num >= n)
                    num /= 10;
                num += 1;
            }
        }

        return ans;
    }
};
```
