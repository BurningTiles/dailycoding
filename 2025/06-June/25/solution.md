# Solution - 25 Jun 2025

---
## [2040. Kth Smallest Product of Two Sorted Arrays](https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays)

### cpp
```cpp
class Solution {
public:
    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        long long l=-1e10, r=1e10, mid=0;

        while(l<r) {
            mid = l + (r-l) / 2;

            if(countProducts(nums1, nums2, mid) < k) l = mid+1;
            else r = mid;
        }

        return l;
    }

    long long countProducts(vector<int> &nums1, vector<int> &nums2, long long target) {
        long long count = 0;

        for(int num1: nums1) {
            if(num1 == 0) {
                if(target >= 0) count += nums2.size();
                continue;
            }

            int low = 0, high = nums2.size();
            while(low < high) {
                int mid = (low + high) / 2;
                long long product = 1LL * num1 * nums2[mid];
                
                if(product <= target) {
                    if(num1 > 0) low = mid + 1;
                    else high = mid;
                } else {
                    if(num1 > 0) high = mid;
                    else low = mid + 1;
                }
            }

            count += (num1 > 0) ? low : nums2.size() - low;
        }

        return count;
    }
};
```
