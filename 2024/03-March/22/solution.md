# Solution - 22 Mar 2024

---
## [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list)

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
    bool isPalindrome(ListNode* head) {
        ListNode *prev = NULL, *cur = head, *next, *fast=head;

        while(fast != NULL && fast->next != NULL) {
            fast = fast->next->next;
            
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }

        if(fast)
            cur = cur->next;
        
        while(prev && cur) {
            if(prev->val != cur->val) return false;
            prev = prev->next, cur = cur->next;
        }

        return prev == cur;
    }
};
```
