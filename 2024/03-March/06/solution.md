# Solution - 06 Mar 2024

---
## [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle)

### cpp
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *fast=head;
        while(fast && fast->next) {
            fast = fast->next->next;
            head = head->next;
            if(head==fast)
                return true;
        }
        return false;
    }
};
```
