# Solution - 28 Mar 2024

---
## [2958. Length of Longest Subarray With at Most K Frequency](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency)

### cpp
```cpp
class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        int j=0, ans=0, n=nums.size();

        for(int i=0; i<n; ++i) {
            cnt[nums[i]]++;

            while(cnt[nums[i]] > k)
                cnt[nums[j++]]--;
            
            ans = max(ans, i-j+1);
        }

        return ans;
    }
};
```
