# Solution - 23 Mar 2024

---
## [143. Reorder List](https://leetcode.com/problems/reorder-list)

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
    ListNode* reorderList(ListNode* head) {
        vector<ListNode*> v;
        
        while(head) 
            v.push_back(head), head = head->next;
        
        int n = v.size();
        for(int i=0, j=n-1; i<j; ++i, --j)
            v[i]->next = v[j],
            v[j]->next = v[i+1];

        v[n/2]->next = NULL;

        return v[0];
    }

    // ListNode* reverseList(ListNode* head) {
    //     ListNode *prev = NULL, *cur = head, *next;
        
    //     while(cur) {
    //         next = cur->next;
    //         cur->next = prev;
    //         prev = cur;
    //         cur = next;
    //     }
        
    //     return prev;
    // }

    // void reorderList(ListNode* head) {
    //     ListNode *slow=head, *fast=head->next, *l1 = head, *next;
        
    //     while(fast && fast->next)
    //         slow = slow->next,
    //         fast = fast->next->next;
        
    //     ListNode *l2 = reverseList(slow->next);
    //     slow->next = NULL;

    //     while(l1 && l2) {
    //         next = l2->next;
    //         l2->next = l1->next;
    //         l1->next = l2;
    //         l1 = l2->next;
    //         l2 = next;
    //     }
    // }
};
```
