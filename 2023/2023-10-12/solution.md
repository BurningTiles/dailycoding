# Solution - 12 Oct 2023

---
## [1095. Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array)

### cpp
```cpp
/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int n = mountainArr.length();
        int s = 1, e = n-2, mid, tmp;
        while(s<e) {
            mid = (s + e) / 2;
            if(mountainArr.get(mid) < mountainArr.get(mid + 1))
                s = mid + 1;
            else
                e = mid;
        }
        int peak = s;

        s = 0, e = peak;
        while(s <= e) {
            mid = (s + e) / 2, tmp = mountainArr.get(mid);
            if(tmp==target) return mid;
            if(tmp < target) s = mid + 1;
            else e = mid - 1;
        }

        s = peak + 1, e = n-1;
        while(s <= e) {
            mid = (s + e) / 2, tmp = mountainArr.get(mid);
            if(tmp==target) return mid;
            if(tmp > target) s = mid + 1;
            else e = mid - 1;
        }
        
        return -1;
    }
};
```
