# Solution - 12 Mar 2024

---
## [1171. Remove Zero Sum Consecutive Nodes from Linked List](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list)

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
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode* ans = new ListNode(0, head), *ptr = ans;

        while (ptr) {
            int sum = 0;
            ListNode *end = ptr->next;

            while (end) {
                sum += end->val;
                if (sum == 0)
                    ptr->next = end->next;
                end = end->next;
            }

            ptr = ptr->next;
        }
        return ans->next;
    }
};
```
