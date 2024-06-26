# Solution - 07 May 2024

---
## [2816. Double a Number Represented as a Linked List](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list)

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
    int helper(ListNode *node) {
        if(node) {
            int digit = node->val * 2 + helper(node->next);
            int carry = digit / 10;
            node->val = digit % 10;
            return carry;
        }
        return 0;
    }

    ListNode* doubleIt(ListNode* head) {
        int carry = helper(head);
        if(carry) return new ListNode(carry, head);
        return head;
    }
};
```
