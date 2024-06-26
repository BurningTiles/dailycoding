# Solution - 06 May 2024

---
## [2487. Remove Nodes From Linked List](https://leetcode.com/problems/remove-nodes-from-linked-list)

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
    ListNode* removeNodes(ListNode* head) {
        vector<ListNode*> stk = {new ListNode(INT_MAX)};

        while(head) {
            while(stk.size() && head->val > stk.back()->val)
                stk.pop_back();
                
            stk.back()->next = head;
            stk.push_back(head);
            head = head->next;
        }

        return stk[0]->next;
    }
};
```
