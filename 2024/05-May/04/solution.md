# Solution - 04 May 2024

---
## [881. Boats to Save People](https://leetcode.com/problems/boats-to-save-people)

### cpp
```cpp
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int i=0, j=people.size()-1, ans = 0;

        while(i<=j) {
            if(people[i]+people[j] > limit) ++ans, --j;
            else ++ans, ++i, --j;
        }

        return ans;
    }
};
```
