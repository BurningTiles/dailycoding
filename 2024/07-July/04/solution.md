# Solution - 04 Jul 2024

---
## [2181. Merge Nodes in Between Zeros](https://leetcode.com/problems/merge-nodes-in-between-zeros)

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
    ListNode* mergeNodes(ListNode* head) {
        ListNode *left = head, *right = head->next;

        while(right) {
            if(right->val == 0 && right->next)
                left = left->next, left->val = 0;
            else
                left->val += right->val;
            
            right = right->next;
        }
        left->next = nullptr;

        return head;
    }
};
```
