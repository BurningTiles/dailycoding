# Solution - 24 Jun 2024

---
## [995. Minimum Number of K Consecutive Bit Flips](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips)

### cpp
```cpp
class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int ans = 0;
        queue<int> q;

        for (int i = 0; i < nums.size(); ++i) {
            if (q.size() && q.front() == i)
                q.pop();

            int val = q.size() & 1 ? !nums[i] : nums[i];

            if (val == 0 && i + k > nums.size())
                return -1;

            if (val == 0) {
                ++ans;
                q.push(i + k);
            }
        }

        return ans;
    }
};
```
