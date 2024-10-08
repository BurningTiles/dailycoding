# Solution - 12 Aug 2024

---
## [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream)

### cpp
```cpp
class KthLargest {
    priority_queue<int, vector<int>, greater<int>> pq;
    int size;
public:
    KthLargest(int k, vector<int>& nums) {
        size = k;

        for(int i=0; i<nums.size(); ++i) {
            pq.push(nums[i]);
            if(pq.size() > size)
                pq.pop();
        }
    }
    
    int add(int val) {
        pq.push(val);
        if(pq.size() > size)
            pq.pop();
        return pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
```
