# Solution - 05 Nov 2023

---
## [1535. Find the Winner of an Array Game](https://leetcode.com/problems/find-the-winner-of-an-array-game)

### cpp
```cpp
class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        int count = 0, i = 0, j = 1;
        while(j<arr.size()) {
            if(arr[i]>arr[j]) ++j, ++count;
            else count = 1, i = j++;
            if(count == k) return arr[i];
        }
        return arr[i];
    }
};
```
