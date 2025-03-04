# Solution - 16 Dec 2024

---
## [3264. Final Array State After K Multiplication Operations I](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i)

### cpp
```cpp
class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

        for(int i=0; i<nums.size(); ++i)
            pq.push({nums[i], i});
        
        while(k--) {
            auto p = pq.top(); pq.pop();
            nums[p.second] *= multiplier;
            pq.push({nums[p.second], p.second});
        }

        return nums;
    }
};
```
