# Solution - 18 Nov 2023

---
## [1838. Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element)

### cpp
```cpp
auto init = [](){ios::sync_with_stdio(0); cin.tie(0); cout.tie(0); return 0;}();

class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        long long n=nums.size(), j=0, sum = 0, ans = 1, sum1;
        
        for(int i=0; i<n; ++i) {
            sum += nums[i], sum1 = nums[i]*(i-j+1);
            while(sum1-sum > k)
                sum -= nums[j++], sum1-=nums[i];
            ans = max(ans, i-j+1);
        }

        return ans;
    }
};
```
