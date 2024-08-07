# Solution - 05 Jul 2024

---
## [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points)

### cpp
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        int first = 0, last = 0, mn = INT_MAX, mx = INT_MIN, cnt = 1;
        ListNode *prev = head, *cur = head->next;

        while (cur && cur->next) {
            if ((cur->val > cur->next->val && cur->val > prev->val) ||
                (cur->val < cur->next->val && cur->val < prev->val)) {
                if(first && last) {
                    mn = min(mn, cnt - last);
                    mx = max(mx, cnt - first);
                }
                
                last = cnt;
                if (!first)
                    first = cnt;
            }

            ++cnt;
            prev = cur;
            cur = cur->next;
        }

        if(mn != INT_MAX)
            return {mn, mx};
        return {-1, -1};
    }
};
```
