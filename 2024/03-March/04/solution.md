# Solution - 04 Mar 2024

---
## [948. Bag of Tokens](https://leetcode.com/problems/bag-of-tokens)

### cpp
```cpp
class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(), tokens.end());
        int i=0, j=tokens.size()-1, curScore = 0, ans = 0;

        while(i<=j) {
            if(tokens[i] <= power) {
                power -= tokens[i];
                ++curScore, ++i;
            }
            else if(curScore) {
                power += tokens[j];
                --curScore, --j;
            }
            else break;
            ans = max(ans, curScore);
        }

        return ans;
    }
};
```
