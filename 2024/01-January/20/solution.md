# Solution - 20 Jan 2024

---
## [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums)

### cpp
```cpp
class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        arr.insert(arr.begin(), INT_MIN);
        arr.push_back(INT_MIN);
        stack<int> stk;
        long long ans = 0;

        for(int i=0; i<arr.size(); ++i) {
            while(stk.size() && arr[stk.top()] > arr[i]) {
                int cur = stk.top(); stk.pop();
                ans += (long long)arr[cur] * (i-cur) * (cur - stk.top());
            }
            stk.push(i);
        }

        return ans % 1000000007;
    }
};
```
### py
```py
class Solution:
    def sumSubarrayMins(self, A):
        res = 0
        stack = []  #  non-decreasing 
        A = [float('-inf')] + A + [float('-inf')]
        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
                cur = stack.pop()
                res += A[cur] * (i - cur) * (cur - stack[-1]) 
            stack.append(i)
        return res % (10**9 + 7)
```
