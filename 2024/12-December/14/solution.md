# Solution - 14 Dec 2024

---
## [2762. Continuous Subarrays](https://leetcode.com/problems/continuous-subarrays)

### cpp
```cpp
class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        long long ans = 0;
        deque<int> a, b;

        for(int i=0, j=0; i<nums.size();  ++i) {
            while(!a.empty() && nums[a.back()] >= nums[i])
                a.pop_back();
            while(!b.empty() && nums[b.back()] <= nums[i])
                b.pop_back();
            a.push_back(i);
            b.push_back(i);

            while(nums[b.front()] - nums[a.front()] > 2) {
                ++j;
                if(a.front() < j) a.pop_front();
                if(b.front() < j) b.pop_front();
            }

            ans += i - j + 1;
        }

        return ans;
    }
};
```
