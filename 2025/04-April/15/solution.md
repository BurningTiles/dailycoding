# Solution - 15 Apr 2025

---
## [2179. Count Good Triplets in an Array](https://leetcode.com/problems/count-good-triplets-in-an-array)

### cpp
```cpp
class Solution {
public:
    void update(vector<long long> &bit, int i, long long val, int n) {
        for(++i; i<=n; i+=(i & -i))
            bit[i] += val;
    }

    long long query(const vector<long long> &bit, int i) {
        long long ans = 0;

        for(++i; i>0; i-=(i & -i))
            ans += bit[i];
        
        return ans;
    }

    long long goodTriplets(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        vector<long long> bit1(n + 2, 0), bit2(n + 2, 0), pos(n);

        for (int i = 0; i < n; ++i)
            pos[nums2[i]] = i;
        for (int i = 0; i < n; ++i)
            nums1[i] = pos[nums1[i]];

        long long ans = 0;

        for(int i=n-1; i>=0; --i) {
            int x = nums1[i];
            long long val = query(bit1, n-1) - query(bit1, x);
            long long trip = query(bit2, n-1) - query(bit2, x);

            ans += trip;
            update(bit2, x, val, n);
            update(bit1, x, 1, n);
        }

        return ans;
    }
};
```
