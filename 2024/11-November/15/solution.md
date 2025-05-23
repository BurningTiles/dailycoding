# Solution - 15 Nov 2024

---
## [1574. Shortest Subarray to be Removed to Make Array Sorted](https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted)

### cpp
```cpp
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int n = arr.size(), low = 0, high = n-1;

        while(low < n-1 && arr[low] <= arr[low+1])
            ++low;
        
        if(low == n-1) return 0;

        while(high > low && arr[high] >= arr[high-1])
            --high;

        int ans = min(n-low-1, high), i=0, j=high;

        while(i<=low && j<n) {
            if(arr[i] <= arr[j]) {
                ans = min(ans, j-i-1);
                ++i;
            }
            else
                ++j;
        }

        return ans;
    }
};
```
